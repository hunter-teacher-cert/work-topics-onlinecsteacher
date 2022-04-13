#In Class Demo
#encrypt letters such that capital Z shifted 1 is capital A and lowercase z shifted 1 is lowercase a
def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
  # traverse the plain text
    if(char.isupper()):
    # Encrypt UPPERCASE characters in plain text
    # convert letter into unicode
    # make A unicode 0 by subtracting 65
    # add shift
    # allow wraparound by mod 26
    # make A's unicode 65 again by adding 65
    # convert unicode to letter
      result += chr((ord(char) - 65 + s) % 26 + 65)
    else:
       # Encrypt lowercase characters in plain text
      result += chr((ord(char) - 97 + s) % 26 + 97)
  return result

  #enter alphabetic text without spaces and a desired shift
text = "AZazHelloWorld"
s = 27

encryptedText = encrypt(text,s)

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encrypted Text: " + encryptedText)

#Homework Bell Pepper Version: Write a function that decrypts a symmetric cipher with a given shift
s = -1

def decrypt(text,s):
  result = ""

  # traverse the plain text
  for i in range(len(text)):
      char = text[i]

      # Decrypt UPPERCASE characters in plain text
      if(char.isupper()):
          result += chr((ord(char) - 65 + s) % 26 + 65)
      else:
       # Decrypt lowercase characters in plain text
        result += chr((ord(char) - 97 + s) % 26 + 97)

    # Once out of the for loop, return the concatenated result
  return result

print("Encrypted Text : " + encryptedText)
print("Shift pattern : " + str(s))
print("Decrypted Text: " + decrypt(encryptedText,s))
