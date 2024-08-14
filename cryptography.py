import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)#make the key in a random order

#print(chars)

#Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
for i in plain_text:
    index = chars.index(i)
    cipher_text+=key[index]

print(f"Original Message: {plain_text}")
print(f"encrypted Message: {cipher_text}")


#Decryption
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""
for i in cipher_text:
    index = key.index(i)
    plain_text+=chars[index]

print(f"encrypted Message: {cipher_text}")
print(f"Original Message: {plain_text}")

