
import random

char = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

long = int(input("Total Number of passwords?"))

for p in range(long):
    length = int(input("Password Length?"))
    password = ''
    for c in range(length):
        password += random.choice(char)
    print(password)

