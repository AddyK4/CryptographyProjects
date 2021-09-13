# This is assignment 1 python code for Cryptography course 3626. The purpose of this assignment is to develop 3
# functions that can convert texts into their equivalent representations or forms. Function 1 consist of string to
# list of characters, function 2 list of characters to ASCII integers, and function 3 ASCII integers to binary form
# Each function can also check the format or type of input so that the conversion process can be done vice versa (binary
# form to ASCII in function 3 for example).
# At start of runtime, user can select a word or multiple words to be converted and the python program will output the
# converted form. The current function will then call again to show the input converted back to it's original form and
# follow up with the next function demonstration till it reaches the last function demonstration.
print("Input a string: ")
word = input("")
print("\nFunction 1", '-' * 50)


def function1(word1):
    if type(word1) is str:  # check if the input is type string
        strList = []
        for i in word1:
            strList.append(i)
        return strList
    elif type(word1) is list:  # check is the input is type list
        strWord = ""
        for i in word1:
            strWord += i
        return strWord
    else:
        print("Error match for input. Input is type", type(word1))


# print the input string, run the function once to show string converted to list, and called again to show the function
# can convert the list back to string
print(word)
word = function1(word)
print(word)
word = function1(word)
print(word)
print("\nFunction 2", '-' * 50)


def function2(list2):
    updatedList = []
    if type(list2[0]) is str:  # Checks if the first element in the list is type string
        for i in list2:
            updatedList.append(ord(i))  # function ord takes in characters and converts it into unicode ASCII int.
        return updatedList
    elif type(list2[0]) is int:  # Checks if the first element in the list is type integer
        for i in list2:
            updatedList.append(chr(i))  # function chr takes in integers and converts it to its ASCII char equivalent
        return updatedList
    else:
        print("Error match for input. First element in input list is not of type string or integer")


# Call function 1 onto a new variable to fulfill the pre-condition for function 2, and show function 2 that the input
# can convert between list of characters and ASCII integers
list0 = function1(word)
print(list0)
list0 = function2(list0)
print(list0)
list0 = function2(list0)
print(list0)
print("\nFunction 3", '-' * 50)


def function3(list3):
    isBinary = False  # isBinary boolean is used to check if the elements of the input list is of type Binary or not
    updatedList = []
    for i in str(list3[0]):  # for loop takes the 1st element and scans the element
        if i in '01':  # if the element contains a 01 anywhere on the element
            isBinary = True  # the list contains binary values
        else:
            isBinary = False  # the list contains non-binary values
    # print(isBinary)
    if isBinary is False:
        for i in list3:
            updatedList.append("{:08b}".format(i))  # followed the documentation for format from the python3 library
        return updatedList
    elif isBinary is True:
        for i in list3:
            updatedList.append(int(i, 2))  # followed the documentation for int conversion from the python3 library
        return updatedList
    else:
        print("Error match for input. First element in input list is not of type string of binaries or an integer")


list1 = function2(list0)
print(list1)
list1 = function3(list1)
print(list1)
list1 = function3(list1)
print(list1)
