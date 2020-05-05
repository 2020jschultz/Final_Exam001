"""  
    For this problem you will modify a function that creates a password
    the password needs to include features from the input list
    that contains information about the person.
    Passwords need to have 3 random special characters
    contain jumbled strings from the input
    include 2-4 numbers
    be of lenght 18-36 characters
    NOTE: 0 points if when you run the code again, the password is similar.
          Every time you run the code you should get a unique string. 
"""
import random
import string

def passwordGenerator(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

print(passwordGenerator(int(input('How many characters are there in your password?'))))
