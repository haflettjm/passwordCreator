'''
    Strong password generator:
        1) Store a List of the characters on a keyboard
        2) Ask for the length of the password
            - Research a good minimum character length for a password.
        3) Shuffle the characters
        4) Iterate length times to generate the password.
        5) choose a random character
        6) add the random character to the password
        7) output a list of passwords
            - Figure out how many you would like to load
        8) Join to create a string from the list of passwords?
        9) print the password?
            - Maybe output it to a file
'''
import string
import random


def inputPassword():
    # get user input and make sure it is at least 11 characters long.
    user = int(input('Hi please input the desired length of the password The minimum is 11 characters: \n'))
    if user < 11:
        user = int(input('Please try again the minimum required length is 11 characters:\n'))
    return user

def passwordMaker(length):
    #blank variable for the creation of the password

    strings = ''

    #while the number is less then the desired length pick a character at random and add it to our password variable
    while len(strings) < length:
        strings += random.choice(character_List)
        #Make sure to remove white spaces
        strings.replace(" ", "")
    return strings

if __name__ == '__main__':
    #assign a list to all characters on a keyboard
    character_List = list(string.punctuation) + list(string.ascii_letters) + list(string.digits)

    #assign the desired length to a variable
    length = inputPassword()

    #shuffle the list so it adds randomness
    random.shuffle(character_List)

    #create the new password and assign it
    passwordCreated = passwordMaker(length)

    #output the newly created password.
    print(passwordCreated)
