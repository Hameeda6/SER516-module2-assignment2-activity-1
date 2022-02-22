import sys

def encrypt(text,s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      elif (char.islower()):
         result += chr((ord(char) + s - 97) % 26 + 97)
         
      else: 
          result+=char

    return result
#check the above function



LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
txt = "CEASER MAN is bad"
a = 5
num = 26-a

encrypt_word = sys.argv[1]
decrypt_word = sys.argv[2]


print(" The encrypted text is: "+encrypt(encrypt_word, a))
print(" The decrypted text is: "+encrypt(decrypt_word, num))