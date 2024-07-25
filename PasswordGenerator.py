import random
import string

def generate_password(length: int = 10):
    #basically makes a group of all possible characters on a keyboard
    alpha = string.ascii_letters + string.digits + string.punctuation 
    #Selects a lengths worth of random values from the group of charaters in alpha
    password = ''.join(random.choice(alpha) for i in range(length))
    return password

password = generate_password()#can put in any integer value
print(f"Generated Password: {password}")