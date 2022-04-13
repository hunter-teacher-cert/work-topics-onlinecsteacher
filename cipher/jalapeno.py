##Helpful Functions
#chr(ASCIICODE) --> character
#ord(CHARACTER) --> ASCII value

def encrypt(message,key):
    encrypted=""
    message = message.upper()
    key = key.upper()
    i = 0
    while (i<len(message)): #iterating through the message
        iKey = i%len(key) #index of key string
        #getting each letter's ASCII and converting to 0-25
        p = ord(message[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65

        #vigenere encryption formula per char: C = (P+d)%26
        #adding by d in order to move that many steps ahead
        # include %26 in case you have to wraparound to the start of the alphabet, e.g. W + E = A
        c = chr(((p+d)%26)+65) #add 65 again to get to letters in ascii code
        encrypted+=c
        i+=1
    return encrypted

def decrypt(secret,key):
    decrypted = "" #an empty string to build on

    #make all of your cases upper for both secret and key
    secret = secret.upper()
    key = key.upper()

    #use a while loop to iterate through message and key
    i = 0
    while (i<len(secret)): #iterating through the message
        iKey = i%len(key) #set iKey equal to the index of key string

        #convert both the encrypted char and the key into ASCII codes
        c = ord(secret[i])-65 #ord to convert chr to ascii, 65 due to A's ascii code
        d = ord(key[iKey])-65

        #use the decryption formula of p = (c-d)%26, e.g. -1%26 = 25
        #convert the decrypted ASCII into a character
        p = chr(((c-d)%26) + 65)
        #concatenate on to the decrypted subtracting
        decrypted+=p
        i+=1
    return decrypted

m = "computerscience"
k = "bcd"

#Use this resource to check your work: https://www.dcode.fr/vigenere-cipher

encrypted = encrypt(m,k)
decrypted = decrypt(encrypted,k)

print(encrypted)
print(decrypted)
