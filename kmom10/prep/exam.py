#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions
file = "manifesto.txt"
def analyze_text():
    """
    Test för vokaler, punkter och stora bokstäver
    """
    while True:
        choice = input("--> ")
        if choice == "q" or choice == "quit":
            return True
        elif choice == "v":
            print(analyze_functions.vokaler(file))
        elif choice == "p":
            print(analyze_functions.punkter(file))
        elif choice == "u":
            print(analyze_functions.bigletters(file))
        else:
            print("Not an option!")
    return True

def list_median(values):
    """
    Hitta median från en list
    """
    values = sorted(values)
    length = len(values)
    result = 0
    if length % 2 == 0:
        result = (values[length // 2 - 1] + values[length // 2]) / 2
    else:
        result = values[(length-1) // 2]

    return result

def find_duplicates(values):
    """
    find_duplicates
    """
    values = [word.lower() for word in values]
    pairs = []
    for word in values:
        if values.count(word.lower()) > 1:
            if not word in pairs:
                pairs.append(word)
    return sorted(pairs)

def types(items):
    """
    types
    """
    item_list = []
    for item in items:
        if isinstance(item, int):
            item_list.append("The square of " + str(item) + " is " + str(item * item) + ".")
        elif isinstance(item, str):
            item_list.append("The secret word is " + str(item) + ".")
        elif isinstance(item, list):
            item_list.append("The list contains " + ", ".join(item) + ".")

    result = " ".join(item_list)
    return result

def validate_email(email):
    """
    validate-email
    """
    valid = True
    if email.count("@") == 1:
        email_at = email.find("@")
    else:
        valid = False
        return valid

    if email[0] == "@":
        valid = False

    if not email[email_at+1].isalpha() or email[email_at+1].isdigit():
        valid = False

    email_at_after = email[email_at + 1:]

    if email_at_after.count(".") > 0:
        for pos, char in enumerate(email_at_after):
            if char == ".":
                if email_at_after[pos - 1] == ".":
                    valid = False
    else:
        valid = False
        return valid

    last_dot = email_at_after.rfind(".")
    if not (len(email_at_after[last_dot+1:]) >= 2 and len(email_at_after[last_dot+1:]) <= 3):
        valid = False
        return valid

    for char in email:
        if not ((char in "._-@" or char.isdigit() or char.isalpha())) or char in "åäö":
            valid = False
            return valid

    if not email.islower():
        valid = False
        return valid

    return valid



if __name__ == '__main__':
    analyze_text()
    list_median([])
    find_duplicates([])
    types([])
    validate_email("")
