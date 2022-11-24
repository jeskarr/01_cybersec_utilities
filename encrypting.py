import random
import string
import base64

##################################### UTF, UNICODE, ASCII  #####################################
'''
INTRODUCTION:
ASCII and Unicode are 2 standards which define a set of chars (in ASCII they're just 256, in Unicode around 1M) and also
an encoding (=codifica) of these chars (i.e. mapping the set of char into a value that can be displayed digitally (a "codepoint"), 
basically for each char there is a corrispondent number).
However, usually Unicode is used just to indicate the set of char because there are various unicode encoding: utf-8, utf-16
etc.... So usually we refer to the encoding of Unicode chars with the specific name of the encoding, e.g. UTF-8 which uses 
groups of bytes (e.g. 8 bits) to represent a single char (from 1 to 4 bytes, e.g. 1 byte to represent the same chars that 
ascii represent), basically it converts a Unicode “codepoint” (e.g. U+0000) or hexadecimal integer into a particular sequence of bytes.
'''

'''
So as said in the introduction:
    -To represent a unicode string (i.e. a "normal" string) as a string of bytes is known as "encoding". 
        => python uses the function someUnicodeString.encode(encoding, error) which is in the module String!!!
            ->remember to import string (we've already done before!)
            ->encoding is by default utf-8 but we can specify a different one if we want (e.g. ascii)
            ->error is by default strict (meaning that encoding errors raise exceptions), but we can also 
                put e.g. ignore, replace etc...
    -To convert a string of bytes to a unicode string (i.e. a "normal" string) is known as "decoding".
        => python uses the function someByteString.decode(encoding, error) which is in the module String!!!
            ->remember to import string (we've already done before!)
            ->encoding specifies the encoding on the basis of which decoding has to be performed
N.B. a string of bytes is diplayed in python as b'unicodestring', but it's actually not printable.
N.B. they do NOT modify the string, they return it
'''
def toByteString(text):
    enc_text = text.encode()
    return enc_text

def toUnicodeString(byte_str):
    dec_str = byte_str.decode()
    return dec_str

'''
Python ord() and chr() are built-in functions (no need to import any library). 
They are used to convert a character to an int and vice versa:      
    -ORD(char)   => returns an integer (in decimal base) which is the Unicode code point value
        N.B. takes a SINGLE (unicode) char
    -CHR(number) => returns a char (is the unicode char corrispondent of that number)
Python ord() and chr() functions are exactly opposite of each other.
'''
#Function with transform the char given into an int and the int given into a char
    #N.B. the integer is the decimal value of the Unicode code point value
def UnicodeConv(char = "a", number = 120):       #"a" and 120 are default values  
    print(char, "=>", ord(char))
    print(number, "=>", chr(number))



##################################### RANDOM NUMBERS #####################################
'''
To generate pseudo-random numbers in python we need to import the "random" module.
To initialize the random number generator we use:
    random.seed()
In particular, if we don't specify any parameter, the current system time is used as seed. 
We can specify, e.g. by putting an int as parameter:
    random.seed(10)
N.B. with this method, as in C, every time we run the program the random number generated
are always the same

N.B. If you don’t initialize the pseudo-random number generator, then the random generator 
uses the OS’s randomness sources to set the seed value. 
'''

'''
Some other useful funcion, after initializing the seed, are:
    -random.choice(someSequence) method returns a randomly selected element from the specified sequence
        N.B. the sequence can be a string, a list, a range, a tuple etc...
    -random.shuffle(someList) method takes a list and reorganize the order of the items in a random way
        N.B. it MODIFY THE give LIST (NOT return another one)
'''
#Function that generate a random psw of n chars (by default 10) (only letters)
def randomPsw(n=10):
    psw = ""

    random.seed()
    for i in range(n):
        psw += random.choice(string.ascii_letters)
    #print("With seed = current time: ", psw)

    '''
    BAD-PRACTICE:
    psw_bad = ""
    random.seed(3)      #fixed seed
    for i in range(n):  
        psw_bad += random.choice(string.ascii_letters)
    print("With seed = 3: ", psw_bad)       #psw_bad is always the same
    '''
    return psw

'''
One way to generate different sequences each time is by putting a different seed each time, this is possible e.g.
using as seed the current time. E.g.:
    cur_time = str(time.time()).encode('ASCII')             
    random.seed(cur_time)  
N.B. time.time() method return the time in seconds since the epoch (i.e. 1/1/1970) as a floating point number
'''

#Some method to return a random number in a given range
'''
N.B. WE NEED TO IMPORT RANDOM FOR THESE METHODS!
Both these following methods return an integer number selected element from the specified range, with some little some differences:
    -random.randrange(start, stop, step), which parameters are:
        ->start, optional, specify at which position to start (default is 0)
        ->stop, required, specify at which position to end (NOT INCLUDED!!!)
        ->step, optional, spceify the incrementation in the range, so the generated random number is divisible by step (default 1)
    e.g. random.randrange(3, 9)     =>      returns a number between 3 (included) and 9 (not included)

    -random.randint(start, stop), which parameters are both required and specify at which position to start and end (END IS INCLUDED!!!)
        ->e.g. random.randint(80, 120)      =>      returns a integer between 80 (included) and 120 (included)
        ->Note: This method is basically an alias for randrange(start, stop+1).
'''



##################################### BASES #####################################
'''
int() function returns an integer from a given object or converts a number in a 
given base to a decimal.
    -int(x, base)
        =>x [optional]: string representation of an integer value, defaults to 0, if no value provided.
            e.g. x = "126"
        =>base [optional]: base of the number (it's the given number i.e. x)
            e.g. if x = "01000100", base = 2 and the int() method returns
N.B. int() returns NOT modify the given string.
'''
def BinToInt(bin):
    return int(bin, 2)

#If long string of binary multiple of 8, most likely binary representation of each char in binary
def BinToChar(bin):
    #divide the binary string in 8-bit blocks (which represent a single char)
    bytes_list = [bin[i*8:i*8+8] for i in range(len(bin)//8)]       

    #trasform each byte (which is in binary) to int and then with chr() we can have
    #the char unicode corrispondentrepresentation
    text = [chr(int(byte, 2)) for byte in bytes_list]

    return "".join(text)

#From a string in hexadecimal format to "normal" (unicode) string
def hex2str(hexStr):
    decList = []
    for i in range(len(hexStr) // 2):         
        hexchar = hexStr[i*2 : (i+1)*2]     #each hex char is formed by 2 simbols  (alternative: hexchar = hexStr[i*2 : i*2+2])
        decList.append(int(hexchar, base=16))      #transform to decimal each hex char (i.e. couple of simbols)
    #declist is a list which elements are integers (each integer represent a char)
    UniStr = ""
    for elem in decList:
        UniStr += chr(elem)
    return UniStr

#From a "normal" (unicode) string to a string in hexadecimal format
def str2hex(uniStr):
    decList = []
    for char in uniStr:
        decList.append(ord(char))
    #decList is a list which elements are the decimal value of each char
    hexstr = ""
    #hex() function converts an integer to the corresponding hexadecimal number in string form and returns it
    for elem in decList:
        hexstr += hex(elem)[2:]     #2: to delete the 0x prefix
    return hexstr



##################################### BASE 64 #####################################
'''
Base64 is a group of binary-to-text encoding schemes that represent a sequence of 8-bit (i.e. bytes) 
into a string composed of base64 alphabet(i.e. “A” to “Z”, “a” to “z”, “0” to “9”, “+” and “/”). 
    -So encoding in base64 is: byte string   =>      base64 string (in BYTES!!!)
        =>we can use the base64.b64encode(byteString) function in python (of the module base63)  
            ->we need to import base64
            ->N.B. it doesn't modify the string but return one
    -So decoding in base64:  base64 string  (in BYTES!!!)  =>      byte string
        =>we can use the base64.b64decode(base64String) function in python (of the module base63)  
            ->we need to import base64
            ->N.B. it doesn't modify the string but return one
N.B. with base64 string we mean a string composed only by “A” to “Z”, “a” to “z”, “0” to “9”, “+” and “/”
    and padding "="

Data encoded in base64 are recognizable because:
    -The length of a Base64-encoded string is always a multiple of 4
    -Only these characters are used by the encryption: “A” to “Z”, “a” to “z”, “0” to “9”, “+” and “/”
    -The end of a string can be padded up to two times using the “=”-character (this character is allowed 
     in the end only, and it's added to in order to have a length which is a multiple of 4)
'''
#Given an unicode string it returns a string encoded in base64
def StrToB64(text):
    '''
    base64.b64encode(Bytestring) accept as parameter a byte string, but we have
    as parameter a "normal" (unicode) string, we need firstly to tranform text
    into a byte string (we've already seen how to do that)
    '''
    text_bytes = text.encode()

    enc_text = base64.b64encode(text_bytes).decode()        #b64encode() returns a byte like object so we need to decode it!

    return enc_text

def B64ToStr(enc_text):
    #b64edcode() accept as parameter a b64 encoded string which is a byte like object!
    dec_bytes = base64.b64decode(enc_text.encode())
    
    #transform byte string into normal unicode string
    text = dec_bytes.decode()

    return text



##################################### XOR #####################################
'''
Xor, also called exclusive or, is a bitwise adn logical operator which output is:
    -1 if the operands are different (i.e. one is 1 and the other is 0)
    -0 when the operands are the same (i.e. both 1 or both 0)
The symbol for XOR in Python is '^', used e.g. xor_num = num1 ^ num2

The XOR operator is placed between two numbers or boolean values.
The XOR operation can be used for different purposes:
    ->XOR of two INTEGERS!
        -it will compare bits of both the integers bit by bit after converting them into binary numbers
        -e.g. 15 ^ 32 = 47, beacuse first ^ transform both 15 and 32 to binary, each bit is xored and the result
            of each bit being xored is then trasform again into integer
        -e.g. more complicated:   key = ''.join([chr(ord(c1) ^ ord(c2)) for c1,c2 in zip(plaintext, ciphertext_dec)])       #we use ord() to get integer and zip() to iterate the lists at the same time
    ->XOR of two booleans
        -do as per definition of XOR
    ->Swapping two numbers using XOR, etc.
        -without using a temporary variable we can use XOR doing:
            a = a ^ b
            b = a ^ b
            a = a ^ b
'''



##################################### CAESAR CIPHER #####################################
#Caesar cipher is a shift cipher, that uses the substitution of a letter by another one further (or before) in the alphabet.
def caesar_cracker(enc_mess, _from = -30, _to = +30):       #since we don't know what is the key let's try various default values (e.g. 30, -30)
    plaintext = ""
    for key in range(_from, _to):
        for c in enc_mess:
            plaintext += chr(ord(c)+key)
        print(f"key: {key}\t text: {plaintext}")
        plaintext = ""



##################################### VIGENERE CIPHER #####################################
#Vigenere cipher is a shift cipher, that substitute each letter of a a letter further in the alphabet.
#This shift is given by a corrispondent char of a key repeated all along the text
def vigenere_cracker(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(97 + (ord(ciphertext[i]) - ord(key[i%len(key)])) % 26)

    return plaintext



def main():
    print(randomPsw())
    UnicodeConv()

    print("\n")
    byte_hello = toByteString("hello")
    print(byte_hello)
    normal_hello = toUnicodeString(byte_hello)
    print(normal_hello)

    print("\n")
    b64_hello = StrToB64("hello")
    print(b64_hello)
    hello = B64ToStr(b64_hello)
    print(hello)

    print("\n")
    binary = "0100010001001"
    print(BinToInt(binary))
    binary_hello="0110100001100101011011000110110001101111"
    print(BinToChar(binary_hello))

    print("\n")
    str_h = "hello"
    hex = str2hex(str_h)
    print(hex)
    print(hex2str(hex))

    print(caesar_cracker("Fdhvdu"))
    print(vigenere_cracker("FMEORCBI", "KEY"))



if __name__ == "__main__":
    main()
