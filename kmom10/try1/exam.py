#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""
import analyze_functions
import date_time_functions
file = "value-of-time.txt"

def analyze_text():
    """
    analyze text
    """
    while True:
        choice = input("--> ")
        if choice == "q" or choice == "quit":
            return True
        elif choice in ("s", "spaces"):
            print(analyze_functions.spaces(file))
        elif choice in ("l", "letters"):
            print(analyze_functions.letters(file))
        elif choice in ("c", "specials"):
            print(analyze_functions.specials(file))
        else:
            print("Not an option!")
    return True

def validate_mobile(number):
    """
    mobile
    """
    valid = True
    if not len(number) == 13:
        valid = False
        return valid

    start = ["070", "072", "073", "076", "079"]
    if not number[0:3] in start:
        valid = False
    after_start = number[3:]

    if not after_start[0] == "-":
        valid = False
    try:
        for num in after_start[1:4]:
            if not num.isdigit():
                valid = False
        if not after_start[4] == " ":
            valid = False
        for num in after_start[5:7]:
            if not num.isdigit():
                valid = False
        if not after_start[7] == " ":
            valid = False
        for num in after_start[8:10]:
            if not num.isdigit():
                valid = False
    except ValueError:
        valid = False
    return valid


def verify_credit_card(number):
    """
    credit cart validity
    """
    valid = False
    ctrl = number[-1]
    left = number[:-1]
    listleft = []
    newlist = []
    sumnum = []

    for i in left:
        listleft.append(int(i))
    for i, c in enumerate(listleft):
        if i % 2 == 0:
            newlist.append(c * 2)
        else:
            newlist.append(c)
    for num in newlist:
        if num > 9:
            num = 1 + num % 10
            sumnum.append(num)
        else:
            sumnum.append(num)

    sumnum = sum(sumnum)*9
    sumnum = str(sumnum)

    if sumnum[-1] == ctrl:
        valid = True

    return valid

def find_difference(items, items2):
    """
    Find difference
    """
    items = [word.lower() for word in items]
    items2 = [word.lower() for word in items2]

    no_pair = []
    for word in items:
        if not word in items2:
            if not word in no_pair:
                no_pair.append(word)

    for word in items2:
        if not word in items:
            if not word in no_pair:
                no_pair.append(word)

    return sorted(no_pair)

def validate_date_time():
    """
    time and date
    """
    while True:
        choice = input("--> ")
        if choice == "q" or choice == "quit":
            return True
        elif choice in ("d", "date"):
            print(date_time_functions.datetest(file))
        elif choice in ("t", "time"):
            print(date_time_functions.timetest(file))
        else:
            print("Not an option!")
    return True

if __name__ == '__main__':
    analyze_text()
    validate_mobile("")
    verify_credit_card("")
    find_difference([], [])
    validate_date_time()
