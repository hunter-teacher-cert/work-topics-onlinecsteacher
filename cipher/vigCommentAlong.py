# message is plain text, key is what we use to encrypted
def encrypt(message,key):
    # empty string to be filled with encrypted message
    encrypted=""

    # Force convert all letters into uppercase (simplicity!)
    message = message.upper()
    key = key.upper()

    # initialize while loop to 0
    # while loop to iterate through the plaintext
    i = 0
    while (i<len(message)):
        # key needs a separate index
        # e.g. key = BED, i = 3, len(key) = 3
        iKey = i%len(key)

        # plain text convert from ASCII (char -> num) and shifted by 65 to ensure A is 0
        p = ord(message[i])-65

        # key convert from ASCII (char -> num) and shifted by 65 to ensure A is 0
        d = ord(key[iKey])-65

        # p+d: does the shift, i.e. how many letters ahead do I look
        # %26: loops back to the front of the alphabet as needed
        # +65 undoing shift from line 19 and 22
        # chr: converts unicode into char
        c = chr(((p+d)%26)+65)

        # concatenate to our empty string that we're building on
        encrypted+=c
        i+=1
    return encrypted
