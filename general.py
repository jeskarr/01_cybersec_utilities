#########################################  EXTERNAL STUFF  ##########################################
'''
We use "import NAME", where NAME is the name of some external libraries/module or one of our other .py files
(in the same directoy), in order to use them. We can import only an element of the module by writing:
"from NAME import NAME_ELEMENT", where "NAME_ELEMENT" is the name of the element we want to use

N.B. If we use external libraries before importing them we need to install it from shell by writing: 
    pip install NAME
'''
import string
import argparse     #to insert arguments before compiling     e.g. path/general.py arguments



#########################################  GLOBAL SCOPE  ############################################
#GLOBAL VARIABLES (variables with global scope, i.e. visible/accessible to every functions)
text = "qwerty"

#IN ORDER TO INSERT ARGUMENTS BEFORE COMPILATION
#definition of an object ot type ArgumentParser whose parameter "description" gives a brief description of what the program does
parser = argparse.ArgumentParser(description="Cybersec_guide")   
'''
Now we fill the object "parser" with information about program arguments (the one given when compiling)
    #the first parameter is the name of the argument
    #we specify then the type (the default is string)
    #the parameter help to specify some infos about the argument
    #the parameter choices include the values that are accepted for these paramter
'''
parser.add_argument("arg1", type=int, help="It's a random integer")       
parser.add_argument("arg2", help="It'a random string")  
parser.add_argument("arg3", type=int, help="Write 0, 1, 2, or 3 (all other strings/values are not accepted", choices=[0, 1, 2, 3])       
#store all arguments in parser.parse_args() to turn them into objects
args = parser.parse_args()
#N.B. to display the help message write ...path/general.py --help (or alternatively--h)
#N.B. if the name of the arguments start with -- we have to specify the name of the argument before it's value


############################################  STRINGS  ############################################
def strings_info():
    '''
    We can look at strings as a list of chars or just as real strings, so we can access each char or 
    with an index or simply by iterating the string:
    '''
    for i in range(len(text)):         #access each char with index
        print(text[i], " ")
    for c in text:       #access each char iterating each char in the string
        print(c)
    ### NOTA: NON è però possibile cambiarne il valore, nè con text[i] nè con c

    print("\n")
    '''
    We can use "in" also to check if a substring or char is in another string (returns a boolean). 
    Alternatively, we can use someString.find() method which also return the index of the string 
    where we can find the substring/char (if it's not present it returns -1)
    '''
    print("l" in text)      #return False because "l" isn't in the string "qwerty"
    print(text.find("l"))    #return -1 because "l" isn't in the string "qwerty"
    print("er" in text)      #return True because "er" is in the string "qwerty"
    print(text.find("er"))   #return 2 because "er" is in "qwerty" and it starts at index = 2

    print("\n")
    '''
    String manipulation:
        -someString.upper() method returns a string where all characters are in upper case 
            => NOT modification of someString, but return another string!

        -someString.lower() method returns a string where all characters are in lower case
            => NOT modification of someString, but return another string!

        -someString.capitalize() method returns a string where the first character is converted to upper case
            => NOT modification of someString, but return another string!

        -someString.strip() method removes any leading (spaces at the beginning) and trailing 
         (spaces at the end) characters. (N.B.: space is the default leading character to remove, 
         if we want to remove other chars e.g. "." we write someString.strip("."))
            => NOT modification of someString, but return another string!

        -someString.replace("old", "new") method replace any given substring/char with another 
         specified substring/char, e.g. in someString we replace all occurencies of "old" with "new"
            => NOT modification of someString, but return another string!
    '''
    print(text.upper())     #prints "QWERTY"
    print(text.lower())     #prints "qwerty"
    print(text.capitalize())    #prints "Qwerty"
    print(text.strip("q"))      #prints "werty"
    print(text.replace("r", "F"))   #prints "qweFty"
    print(text)     #prints "qwerty" => all above methods don't modify text (they return another modified string)

    print("\n")
    '''
    To concatenate more strings we can simply use +
    '''
    text2 = "uiop"
    print(text+text2)

    print("\n")
    '''
    From the library "string" (so we must do: import string), we can recover some useful constants:
        -string.ascii_letters, is the concatenation of the ascii_lowercase and ascii_uppercase constants
        -string.ascii_lowercase, is the string 'abcdefghijklmnopqrstuvwxyz' (e.g. all lower case letters)
        -string.ascii_uppercase, is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' (e.g. all upper case letters)
        -string.digits, is the string '0123456789'.
        -string.punctuation, is the string !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (all ASCII chars considered punctuation)
        -string.printable, is a string which is the combination of digits, ascii_letters, punctuation, and whitespace
    '''
    print(string.ascii_letters)
    print(string.ascii_letters == (string.ascii_lowercase+string.ascii_uppercase))
    print(string.digits)
    print(string.printable)
    print(string.punctuation)


############################################  LISTS  ############################################
def lists_info():
    sampleList = ["a", "b" ,"c", "d", "e"]
    '''
    SLICING (it works for strings too)
    To access an element of a list we use indexes e.g. someList[2] to access the third element (list 
    indexes start at 0). If we put negative numbers we access starting from the last element, 
    e.g. someList[-1] is the last element of the list
    We can also take a "slice" of the list e.g. somelist[4:6] where we take the element from index 4 
    included to 6 EXCLUDED. If we don't specify the starting index is 0 by default, and if we don't 
    specify the ending index the slice end at the end of the list
    '''
    print(text[1])      #prints w (indexes start at 0)
    print(text[-1])    #prints y (last char)

    print(sampleList[1:3])     #prints ["b", "c"]       (ending index of the slice is excluded)
    print(sampleList[:2])      #prints ["a", "b"]       (ending index of the slice is excluded)
    print(sampleList[-2:])     #prints ["d", "e"]

    '''
    STRING => LIST
    someString.split() return a list which is the result of splitting someString and each piece is
    a different element in the list. By default, the separator (the char who causes the splitting)
    is any whitespace (so every time there is a whitespace in the string, this method create a new
    element in the returned list). You can specify the separator simply by specifying it inside (),
    e.g. someString.split(",") splits someString every time it encounters the comma
    N.B. the separator is NOT included in the returned list

    LIST => STRING
    The "separator".join(someList) method takes all items in an iterable (i.e. the list, a tuple etc... 
    N.B. if dict it joins only keys), in this case someList, and joins them into one string, separating 
    each element of the list with the given separator, which is then returned
    '''
    print(text.split("e"))      #returns the list ["qw", "rty"]
    print("-".join(sampleList))
    
    '''
    2 ways of creating a list, it's easier to explain with an example:
        =>we want to create a list which elements are the elements of fruits which contain an "a"
    '''
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    #1st WAY: without list comprehensione
    newlist = []
    for x in fruits:
        if "a" in x:
            newlist.append(x)
            #N.B. someList.append(new_elem) MODIFIES someList by adding at the end of it a 
            #new element, which is new_elem           
    print("without list comprehension: ", newlist)

    #2nd WAY: with list comprehension:      sintax =>  newlist = [EXPRESSION for ITEM in ITERABLE if CONDITION]
    #NB: ITEM is the single element of ITERABLE (the list from which we take the elements), CONDITION is NOT
        #mandatory, and it's the condition that must be satisfied in order to add EXPRESSION to the list, EXPRESSION
        #is the new element which will be added to the newlist (usually is the same as ITEM or some manipulation)
    newlist2 = [x for x in fruits if "a" in x]
    print("with list comprehension: ", newlist2)


############################################  FILES  ############################################
def files_info():
    '''
    To open a file there are 2 ways:
        - f = open("path/someFile", "MODE")
            ->f is how we call the file in our code (we will call it nameOfFileInCode)
            ->MODE is how we open the file: "r" is for reading, "w" for writing etc...  
            ->N.B. the path can be omitted if someFile is in the same directory
        !!!->NB. if we use this method WE MUST CLOSE THE FILE with f.close() 
        -with open("path/someFile", "MODE") as f:
            #code
            ->the file closes automatically once we exit the with statement
    '''
    #WRITING A FILE: 2 ways        
    #=> nameOfFileInCode.write(someString) method writes the string in the file
    lines = ['writeme', 'How to write text files in Python']  
    stringAlone = "string here is alone"
    with open('useful_tools/samplefile.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
        f.write(stringAlone)
    #=> nameOfFileInCode.writelines(someList) method writes the items of a list to the file 
        #(in the same line, in order to have each element in a new line, we need to have \n in the list)
    with open('useful_tools/samplefile2.txt', 'w') as f:
        f.writelines(lines)

    #READING A FILE => 2 ways
    #=> someString = nameOfFileInCode.read() method return one long list (in this case stored in someString)
    f = open("samplefile.txt", "r")   
    fileString = f.read()   
    f.close()
    print(fileString)
    #=> someList = nameOfFileInCode.readlines() method return all lines in the file as a list 
        #where each line is an item in the list object  (in this case stored in someList)
    with open('samplefile.txt', 'r') as f:
        linesList = f.readlines()
    print(linesList)


##########################################  EXCEPTIONS  ##########################################
def exception_info():
    '''
    To interrupt the execution of a program we can raise a generical Exception by writing:
    raise Exception("Specify here the reason of the exception)
    e.g. we ask for a number < 5 in input, if it's not, we'll raise an exception
    '''
    x = float(input("Type a value < 5: "))
    if x >= 5:
        raise Exception("the value in input is >= 5 and not < !")

    '''
    In addition to generate them, it is also possible to catch the system ones by writing:
    try:
        #expression that may cause a system exception
    except:
        #code to be executed if the system exception happens
    N.B. in this case the system exception does NOT cause the interruption of the program !!!
    '''
    try:
        with open('file.log') as file:    #we're trying to read a file that doesn't exist => system expection FileNotFound
            read_data = file.read()
    except:
        print('Could not open file.log')
        a = 5
    '''
    Usually is a good practice to specify the type of the system exception, so that if the code in try: ...
    raises different types of exception, for each type we can execute a specified code e.g.:
    try: 
	    #expression that may cause 2 types of system exception
    except Type1 as Name1error:
        #code to be executed if the system exception of Type1 happens
    except Tipo2 as Name2error:
        #code to be executed if the system exception of Type2 happens
    N.B. Name1error is the name we gave to the error if it's not specified is the default one
    '''
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        fnf_error = "File doesn't exist. This is my custom message for the error."
        print(fnf_error)



def main():
    strings_info()
    print("\n\n")

    lists_info()
    print("\n\n")

    files_info()
    print("\n\n")
    
    exception_info()
    print("\n\n")
    
    someInt = args.arg1       #take the argument arg1 from the shell and store it in someInt
    someString = args.arg2
    number0123 = args.arg3
    print(f"The arguments in input before compilation: {someInt}, {someString}, {number0123}")
    print("\n\n")

    '''
    To print a string with variables in it we can use {} inside the stringToPrint and:
        ->"stringToPrint".format(variables)
    or
        ->f"stringToPrint" and the variables inside the {}
    '''
    print(f"Fred scored {3} out of {10} points.")
    print("Fred scored {} out of {} points.".format(3,10))
    #In particular, we can also use .format() as:
    msg2 = 'Fred {verb} a {adjective} {noun}.'
    print(msg2.format(adjective='fluffy', verb='tickled', noun='hamster'))
    


#to execute only the "main()", we'll need to write this at the end of the file
if __name__ == "__main__":
    main()
