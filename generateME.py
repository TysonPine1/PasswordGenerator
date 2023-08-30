import random 
import string

def password_generator(min_length, max_length, special_characters = True, numbers = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special_characters = False

    while not meet_criteria or len(pwd) < min_length or len(pwd) > max_length:
        new_char = random.choice(characters)
        pwd  += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special_characters = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special_characters

    return pwd

min_length = int(input("Enter the minimum length(letters): "))
max_length = int(input("Now, it's the maximum length(letters): "))
has_number = input("Do you want to put in number(Y/N)?: ").lower() == 'y'
has_special_characters = input("Do you want to put in special characters(Y/N)?: ").lower() == 'y'
pwd = password_generator(min_length, max_length, has_number, has_special_characters)
print("Here's your passowrd: ", pwd)