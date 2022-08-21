import random 
import string

# Simple XOR Encryption


def xorEnc(contents, key):

    encContents = "".join([chr(ord(c) ^ ord(k)) for (c, k) in zip(contents, key)])

    # We utilize list comprehension to perform an XOR function ^ for each unicode character's integer 'ord()' in the contents and then convert back to unicode characters
    # This is because the XOR function requires integer values to work
    # We use the zip() function to pair each character in the contents to the corresponding key character in its index


    return encContents, key

    # Don't forget to save your key!
    # Because XOR is a symmetric form of encryption, you can utilize the same function with the same key to decrypt


# Example

if __name__ == '__main__':

    contents = "Thanks for checking out this script!"


    key = "".join(random.choices(list(string.ascii_letters + string.digits), k = len(contents))) 

    # Sets the key to a random string made up of letters and numbers of the same length as the contents
    # It is important that the key is the same length or longer in order to pair indeces properly with the zip() function


    xorContents, xorKey = xorEnc(contents, key)


    decContents, xorKey = xorEnc(xorContents, key)
    # Just to show the symmetric encryption property

    
    print(f"XOR Contents: {xorContents}\n\n")
    
    
    print(f"XOR Key: {xorKey}\n\n")

    
    print(f"Contents Decrypted: {decContents}")
