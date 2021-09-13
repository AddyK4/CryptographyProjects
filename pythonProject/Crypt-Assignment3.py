# This is assignment 3 python code for Cryptography course 3626 - Feistel Cipher. The purpose of this assignment is to
# develop a program that replicates the encryption process of a Feistel Cipher but with limitations of only 1 round. The
# input would be string that represents a plaintext and any integer called key that is used to formulate the Feistel
# cipher's encryption (2 * Right half side of the binary input to the key, modulus 2 to the 4th). The list of encrypted
# binaries will then be used to generate a encrypted word that takes reference with the ASCII table using the functions
# developed from assignment 1.

print("Input a string: ")
word = input("")
word = word.replace(" ", "")
print("Input any integer for the key: ")
key = int(input())


def feistelCipher(bits, k):  # Step 1
    # Step 2
    leftSide = bits[0:4]
    rightSide = bits[4:8]

    # Step 3
    rightSideDecimal = int(rightSide, 2)
    feistelFunction = 2 * rightSideDecimal ** k % 16
    rightSideFunction = format(feistelFunction, '04b')

    cipherLeft = rightSide
    cipherRight = xOR(leftSide, rightSideFunction)

    # Step 4
    leftSide = cipherRight
    rightSide = cipherLeft

    # On this assignment, step 4 read as 𝑅_1||𝐿_1 which I assumed after swap, it would return right side then left side
    # Just wanted to be clear that the right + left was intentional per the instructions read in the assignment
    return rightSide + leftSide


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


def xOR(a, b):
    temp = ""

    for i in range(4):
        if a[i] == b[i]:
            temp += "0"
        else:
            temp += "1"
    return temp


cipherList = function3(function2(function1(word)))
print("The list of 8 bit binary input for the string: \n", cipherList)
updatedList = []

for i in cipherList:
    updatedList.append((feistelCipher(i, key)))

print("The list of 8 bit binary input after Feistel is applied: \n", updatedList)
cipherList = function1(function2(function3(updatedList)))
print("The returned encryption string: \n", cipherList)
