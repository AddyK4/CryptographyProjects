# This is assignment 4 python code for Cryptography course 3626 - RSA. The purpose of this assignment is to develop a
# program that replicates the encryption and decryption process of RSA. The inputs (p, q, and message) for the program
# will be defined within the code and the output will show the plaintext and ciphertext of the message. However, as the
# p, q, and message becomes longer, the run time will also become longer.

# Functions that short-cut for KeyGen and RSA function
# ----------------------------------------------------------------------------------------------------------------------
def extendedEuclid(a, b):
    if a == b:
        return 1, 0, a
    elif b == 0:
        return 1, 0, a
    else:
        x_1 = 1
        y_1 = 0
        r_1 = a

        x_2 = 0
        y_2 = 1
        r_2 = b

        while r_2 != 0:
            q = r_1 // r_2

            r_t = r_1 - q * r_2
            x_t = x_1 - q * x_2
            y_t = y_1 - q * y_2

            x_1, y_1, r_1 = x_2, y_2, r_2
            x_2, y_2, r_2 = x_t, y_t, r_t

        return x_1, y_1, r_1


def multiplicativeInverse(a, n):
    x, y, r = extendedEuclid(n, a % n)
    if r != 1:
        print("No multiplicative inverse")
        return
    else:
        return y % n


def GCD(a, b):
    while b != 0:
        rem = a % b

        a = b
        b = rem
    return a
# ----------------------------------------------------------------------------------------------------------------------


def keyGen(p, q):
    n = p * q
    phiN = (p - 1) * (q - 1)

    e = 2

    # Search for an e that is co-prime to phi of n
    while GCD(phiN, e) != 1:
        e += 1

    # Find d value
    d = multiplicativeInverse(e, phiN)

    PU = (e, n)  # Public key
    PR = (d, n)  # Private key

    # Return public and private keys
    keys = (PU, PR)
    return keys


# RSA function to find ciphertext and plaintext
def RSA(text, key):
    # If first input is str means we have to do encryption
    if type(text) is str:
        M = ord(text)  # ASCII value of the Message text
        ciphertext = (M ** key[0]) % key[1]  # Compute Ciphertext C = M^e mod N
        return ciphertext

    # If first input is int means we have to do decryption
    elif type(text) is int:
        C = (text ** key[0]) % key[1]  # Compute Message M = C^d mod N
        plaintext = chr(C)  # ASCII value to text
        return plaintext
    else:
        raise Exception("Invalid Input")


# Test ----------------------------------------------------------------------------------------------------------------
# Define p, q, and the original message
p = 7907  # Answer for step 5: So I used prime numbers up to 7907 and 7919, and it seemed that my computer can
q = 7919  # still handle it. But the decryption time becomes exponentially longer due to the exponents of the RSA calc.
message = 'hello'
print("Original Message:", message)

# Generate public key and private key
PU, PR = keyGen(p, q)
print("Public key:", PU)
print("Private key:", PR)

# Perform encryption of letter M <--- Encryption
ciphertexts = []
for M in message:
    ciphertext = RSA(M, PU)
    ciphertexts.append(ciphertext)
print("Ciphertext:", ciphertexts)

# Perform decryption of letter C <--- Digital Signature
plaintexts = []
for C in ciphertexts:
    plaintext = RSA(C, PR)
    plaintexts.append(plaintext)
print("Plaintext:", plaintexts)
# End of Test ----------------------------------------------------------------------------------------------------------
