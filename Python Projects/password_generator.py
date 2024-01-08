#Password Generator
import random
import string 

length = input("Enter length of password required: ")
low = string.ascii_lowercase
upp = string.ascii_uppercase
num = string.digits
sym = string.punctuation
chars = low + upp + sym + num
temp = random.sample(chars, int(length))
final = "".join(temp)
print("Generated Password:")
print(final)