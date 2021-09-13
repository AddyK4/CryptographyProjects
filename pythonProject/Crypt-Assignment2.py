# This is Cryptography 3626 assignment 2 - Playfair cipher implementation. The purpose of this assignment is to develop
# 4 functions that all together would output like a Playfair cipher would function itself. "functionKey" involves in
# developing a Key Matrix that the Playfair cipher would use to encrypt a cipher text while "functionPre" takes in a
# english word or sentence to convert it into the cipher text. The Key Matrix and cipher text would then be used as
# input for "functionEnc" and output a list paired with two letters that shows its encrypted text. "functionDec" would
# then take the encrypted text as input and output the ciphertext into string. An extra function named "indexLocation"
# was created to do the major checks with the key and ciphertext for it contained a big complexity that a extra function
# was needed to make the program easier.
def functionKey(encKey):
    result = []
    # print(result)
    for i in encKey:
        if i not in result:
            if i == 'j':
                result.append('i')
            else:
                result.append(i)
    # print(result)

    checkIJ = 0
    for i in range(97, 123):  # checks the ASCII table that ranges a-z
        if chr(i) not in result:
            if i == 105 and chr(106) not in result:
                result.append("i")
                checkIJ = 1
            elif checkIJ == 0 and i == 105 or i == 106:
                pass
            else:
                result.append(chr(i))
    # print(result)

    index = 0
    matrix = [[0 for i in range(5)] for j in range(5)]
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = result[index]
            index += 1
    # print(matrix)
    return matrix


def functionPre(plaintext):
    result = []
    # print(plaintext)
    for i in range(0, len(plaintext)+1, 2):
        if i < len(plaintext)-1:
            if plaintext[i] == plaintext[i+1]:
                plaintext = plaintext[:i+1] + 'x' + plaintext[i+1:]

    if len(plaintext) % 2 != 0:
        plaintext = plaintext[:] + 'x'

    for i in range(0, len(plaintext), 2):
        result.append(plaintext[i] + plaintext[i+1])
    # print(result)
    return result


def indexLocation(char):
    loc = []
    if char == 'j':
        char = 'i'
    for i, j in enumerate(functionKey(encryptionKey)):  # goes through the key matrix
        for k, l in enumerate(j):  # goes through the paired characters that are stored in j
            if char == l:  # checks to see if the char matches with the key
                loc.append(i)  # stores the column index if yes
                loc.append(k)  # stores the row index if yes
                return loc


def functionEnc(KM, PL):
    cipherText = ""
    result = []
    index = 0
    for e in PL:
        cipherText += e
    while index < len(cipherText):
        indexLoc1 = []
        indexLoc1 = indexLocation(cipherText[index])
        indexLoc2 = []
        indexLoc2 = indexLocation(cipherText[index + 1])
        if indexLoc1[1] == indexLoc2[1]:
            result.append("{}{}".format(KM[(indexLoc1[0] + 1) % 5][indexLoc1[1]], KM[(indexLoc2[0] + 1) % 5][indexLoc2[1]]))
        elif indexLoc1[0] == indexLoc2[0]:
            result.append("{}{}".format(KM[indexLoc1[0]][(indexLoc1[1] + 1) % 5], KM[indexLoc2[0]][(indexLoc2[1] + 1) % 5]))
        else:
            result.append("{}{}".format(KM[indexLoc1[0]][indexLoc2[1]], KM[indexLoc2[0]][indexLoc1[1]]))
        index = index + 2
    return result


def functionDec(KM, CL):
    encryptedText = ""
    decryptedText = ""
    result = []
    index = 0
    for d in CL:
        encryptedText += d
    while index < len(encryptedText):
        indexLoc1 = []
        indexLoc1 = indexLocation(encryptedText[index])
        indexLoc2 = []
        indexLoc2 = indexLocation(encryptedText[index + 1])
        if indexLoc1[1] == indexLoc2[1]:
            result.append("{}{}".format(KM[(indexLoc1[0] - 1) % 5][indexLoc1[1]], KM[(indexLoc2[0] - 1) % 5][indexLoc2[1]]))
        elif indexLoc1[0] == indexLoc2[0]:
            result.append("{}{}".format(KM[indexLoc1[0]][(indexLoc1[1] - 1) % 5], KM[indexLoc2[0]][(indexLoc2[1] - 1) % 5]))
        else:
            result.append("{}{}".format(KM[indexLoc1[0]][indexLoc2[1]], KM[indexLoc2[0]][indexLoc1[1]]))
        index = index + 2
    for s in result:
        decryptedText += s
    return decryptedText


encryptionKey = input("Enter the encryption key: ")
encryptionKey = encryptionKey.replace(" ", "")
encryptionKey = encryptionKey.lower()

message = str(input("Enter a message: "))
message = message.replace(" ", "")
message = message.lower()

print("\nKey Matrix Generator Function", '-' * 50)
keyMatrix_example = functionKey(encryptionKey)
print(keyMatrix_example)

print("\nPreprocessing Function", '-' * 50)
cipherText_example = functionPre(message)
print(cipherText_example)

print("\nEncryption Function", '-' * 50)
encryptedText_example = functionEnc(keyMatrix_example, cipherText_example)
print(encryptedText_example)

print("\nDecryption Function", '-' * 50)
decryptedText_example = functionDec(keyMatrix_example, encryptedText_example)
print(decryptedText_example)
