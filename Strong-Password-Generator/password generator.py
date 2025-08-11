import random
import string

A = string.ascii_lowercase
B = string.ascii_uppercase
C = string.digits
D = string.punctuation

combined = C + B + A + D

try:
    plen = int(input('Enter the length of the password : '))
except:
    print('Please enter an integer value only!')
    plen = int(input('Enter the length of the password : '))
    
passwd_list = random.sample(combined, plen)
passwd = "".join(passwd_list)

print(passwd)
