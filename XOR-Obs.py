import random 
import string

# Simple XOR Encryption


def xorEnc1(contents, key):

    encContents = "".join([chr(ord(c) ^ ord(k)) for (c, k) in zip(contents, key)])

    # We utilize list comprehension to perform an XOR function ^ for each unicode character's integer 'ord()' in the contents and then convert back to unicode characters
    # This is because the XOR function requires integer values to work
    # We use the zip() function to pair each character in the contents to the corresponding key character in its index

    return encContents, key

    # Don't forget to save your key!
    # Because XOR is a symmetric form of encryption, you can utilize the same function with the same key to decrypt


def xorEnc2(contents, key):

    length = len(contents)

    for i in range(length):

        contents = (contents[:i] + chr(ord(contents[i]) ^ ord(key)) + contents[i+1:]) 
    
    return contents, key


# Example

if __name__ == '__main__':

    contents = "Thanks for checking out this script!"


    # Using xorEnc1 with len(key) == len(contents)

    key = "".join(random.choices(list(string.ascii_letters + string.digits), k = len(contents))) 

    # Sets the key to a random string made up of letters and numbers of the same length as the contents
    # It is important that the key is the same length or longer in order to pair indeces properly with the zip() function

    encContents, xorKey = xorEnc1(contents, key)

    decContents, xorKey = xorEnc1(encContents, key)
    # Just to show the symmetric encryption property


    print("Method 1: len(key) == len(contents)\n")

    print(f"\tContents: {contents}\n")

    print(f"\tXOR Key: {xorKey}\n")

    print(f"\tXOR Contents: {encContents}\n")
    
    print(f"\tContents Decrypted: {decContents}\n\n")




    # Using xorEnc2() with len(key) == 1

    key = random.choice(string.ascii_letters + string.digits)
    # Sets the key to a random string of length 1

    encContents, key = xorEnc2(contents, key)

    decContents, xorKey = xorEnc2(encContents, key)
    # Just to show the symmetric encryption property


    print("Method 2: len(key) == 1\n")

    print(f"\tContents: {contents}\n")
    
    print(f"\tXOR Key: {xorKey}\n")
    
    print(f"\tXOR Contents: {encContents}\n")
        
    print(f"\tContents Decrypted: {decContents}")
