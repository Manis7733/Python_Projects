import random
import string

def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #print(letters, digits, special)

    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters += special

    pwd =""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_character:
            meet_criteria = meet_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum Length: "))
has_number = input("Do you want to have Number? (Y/n)").lower() == "y"
has_special = input("Do you want th have special characters (Y/n)").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)

print("The generated password is: ",pwd)