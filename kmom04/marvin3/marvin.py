#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
marvin functions
"""

import time
import random

#Start
def quit_program():
    """Exit"""
    print("\nExterminate, Exterminate!\n")
    time.sleep(1)

def username():
    """Users name"""
    name = input("What is your name? ")
    print("\nThe Dalek Emperor says:\n")
    print("Hello %s - you dont seem to be The Doctor " % name)
    print("Choose your option wisely!")

#Return to start
def back():
    """Back to the main menu"""
    print("Restarting...")
    time.sleep(1)

#Celcius till Farenheit
def temp_convert(user_choice):
    """Celcius to farenheit converter"""
    temp = user_choice
    while True:
        try:
            temp = int(temp)
            far = temp * 9 / 5 +32
            print("\n")
            print(str(temp) + " degrees Celcius is " + str(far) + " degrees Farenheit")
            print("\n")
            time.sleep(3)
            break
        except ValueError:
            print("You must type a number!")
            time.sleep(1)
            temp = input("What is the temperature in Celcius?\n")

#Word multiplying
def word_multiply(user_choice1, user_choice2):
    """A word copied a set number of times"""
    word = user_choice1
    multiply = user_choice2
    if word == "":
        print("Nothing to do...")
        print("\n")
    elif multiply == "":
        print("Nothing to do...")
        print("\n")
    else:
        while True:
            try:
                multiply = word * int(multiply)
                print("\n")
                print(multiply)
                print("\n")
                time.sleep(2)
                break
            except ValueError:
                print("You must type a number!")
                multiply = input("How many times should i multiply " +word + "?\n")
    print("Do you want to mask this data?")
    if input("Type yes or no\n") == "yes":
        print("\n")
        mask(multiply)

#Amount and average
def amt_avg(user_choice):
    """The sum of all the entered numbers and the average"""
    number = user_choice

    while True:
        try:
            number = int(number)
            break
        except ValueError:
            print("Only numbers allowed!")
            number = input("Type a number?\n")

    newnumber = 0
    count = 1
    print("Type 'done' to calculate!")
    print("\n")

    while True:
        try:
            newnumber = input("Type another number?\n")
            if newnumber == "done":
                break
            else:
                newnumber = int(newnumber)
                number += newnumber
                count += 1
        except ValueError:
            print("Only numbers allowed!")

    try:
        average = number / count
        print("\n")
        print("Calculating...!")
        time.sleep(1)
        print("\n")
        print("The total is " + str(number) + " and the average is " + str(average))
        print("\n")
        time.sleep(3)
    except ZeroDivisionError:
        print("Nothing to do...")
        print("\n")
        time.sleep(3)

#Number comparison
def num_compare(user_choice):
    """A number is compared with another number to see if there is a difference"""
    lastnumber = user_choice
    newnumber = 0

    while True:
        try:
            lastnumber = int(lastnumber)
            break
        except ValueError:
            print("Only numbers allowed!")
            time.sleep(1)
            print("\n")
            lastnumber = input("The staring number is?\n")

    print("Type 'done' to finish!")

    while True:
        newnumber = input("What number should i compare " + str(lastnumber) + " with?\n")
        print("\n")

        if newnumber == "done":
            print("\n")
            print("Finished")
            print("\n")
            time.sleep(1)
            break
        else:
            try:
                newnumber = int(newnumber)
                if newnumber > lastnumber:
                    print(str(newnumber) + " is bigger than " + str(lastnumber))
                elif newnumber < lastnumber:
                    print(str(newnumber) + " is smaller than " + str(lastnumber))
                else:
                    print(str(newnumber) + " is identical to " + str(lastnumber))
                lastnumber = newnumber
            except ValueError:
                print("Only numbers allowed!")

#Each letter multiplies by 1 more than the last letter aba a-bb-aaa-
def letterply(user_choice):
    """A word is split up into letters and each letter is printed one more time than the last letter"""
    word = user_choice
    while True:
        if word.isalpha():
            break
        else:
            print("You must enter a word!")
            word = input("What word do you want to spread?\n")
    count = 1
    new_word = ""
    for letter in word:
        new_word += letter * count + "-"
        count += 1
    print("\n")
    print(new_word)
    print("\n")
    time.sleep(3)

#Isogram test
def isogram(user_choice):
    """Tests for an Isogram, where a word has no repeating letters"""
    isogramtest = user_choice
    while True:
        print("\n")
        if isogramtest.isalpha():
            break
        else:
            print("You must enter a word!")
            isogramtest = input("What word should i test?\n")

    is_isogram = True
    for letter in isogramtest:
        if isogramtest.count(letter) > 1:
            is_isogram = False
            break

    if is_isogram:
        print("Yes, '" + isogramtest + "' is an isogram!")
        time.sleep(3)
    else:
        print("No, '" + isogramtest + "' is not an isogram!")
        time.sleep(3)
    print("\n")

#Word shaker
def shake(word):
    """A word has its letters randomly mixed around to form a new word"""
    if word == "":
        print("Nothning to do...")
        print("\n")
    else:
        word_array = []

        for letter in word:
            word_array.append(letter)

        new_word = ""
        num_letters = len(word) - 1

        while word_array:
            rndm_letter = random.randint(0, num_letters)
            new_word += word_array[rndm_letter]
            del word_array[rndm_letter]
            num_letters -= 1


        print("\n")
        print(new_word)
        print("\n")
        time.sleep(3)

#Anagram test
def is_anagram(word1, word2):
    """Tests two words to see if the seond word is an anagram of the first word"""
    while True:
        if not word1.isalpha():
            word1 = input("Try again, What is the first word?\n")
        elif not word2.isalpha():
            word2 = input("What word should i compare with?\n")
        else:
            break

    word1_small = word1.lower()
    word2_small = word2.lower()

    if sorted(word1_small) == sorted(word2_small):
        print("\nYes, " + word2 + " is an anagram of " + word1 + ".\n")
    else:
        print("\nNo, " + word2 + " is not an anagram of " + word1 + ".\n")

#Acronym maker
def acronym(words):
    """Makes an acronym from the given word"""
    if words == "":
        print("Nothing to do...\n")
    else:
        is_acronym = ""

        for letter in words:
            if letter.isupper():
                is_acronym += letter

        print("\n" + is_acronym + "\n")

#Hidden Strings
def mask(user_choice):
    """Masks data by only showing the last four digits"""
    mask_len = len(user_choice) - 4
    last4 = user_choice[mask_len:]
    word = "#"
    masked = word * mask_len
    print("\n" + masked + last4 + "\n")
    time.sleep(2)

#Letter match
def letter_match(word1, word2):
    """Letter match, are all the letters of a second word present in the first word?"""
    while True:
        if not word1.isalpha():
            print("You must enter a word to test!")
            word1 = input("What word should i test?\n")
        elif not word2.isalpha():
            print("You must enter a word to comapare with!")
            word2 = input("What word should i compare with?\n")
        else:
            break

    match = True
    for letter in word2:
        if not word1.count(letter):
            match = False
            break

    if match:
        print("Yes, there is a match! All the letters in '" + word2 + "' are present in '" +word1 + "'")
        time.sleep(3)
    else:
        print("No match.  Not all the letters in '" + word2 + "' are present in '" +word1 + "'")
        time.sleep(3)
    print("\n")

#Balance brackets
def balance_test(user_choice):
    """Test if the brackets are in the right order"""
    class Stack():
        """
        Organize date ontop of each other
        """
        def __init__(self):
            """
            Stack
            """
            self.items = []

        def add(self, item):
            """
            add to Stack
            """
            self.items.append(item)

        def remove(self):
            """
            remove from stack, last item
            """
            return self.items.pop()

        def is_empty(self):
            """
            tests if the stack has no items
            """
            return self.items == []

    def balanced_pair(b1, b2):
        """
        Simple comparing function with 2 inputs for testing
        """
        if b1 == "(" and b2 == ")":
            return True
        elif b1 == "{" and b2 == "}":
            return True
        elif b1 == "[" and b2 == "]":
            return True

    s = Stack()
    is_opened = "[{("
    is_closed = "]})"
    balanced = True
    bracket_test = user_choice

    while True:
        retry = False
        while True:
            if bracket_test == "":
                print("Nothing to do...")
            else:
                break

        for bracket in bracket_test:
            if bracket in is_opened:
                s.add(bracket)
            elif bracket in is_closed:
                if s.is_empty():
                    balanced = False
                    break
                else:
                    if not balanced_pair(s.remove(), bracket):
                        balanced = False
                        break
            else:
                retry = True
                break

        if retry:
            print("Not a valid bracket, only use ([{}])")
            print("\n")
            time.sleep(1)
            bracket_test = input("Type in the combination of brackets to test if they are balanced\n")
        elif s.is_empty() and balanced:
            print("Yes, the brackets are balanced!")
            print("\n")
            time.sleep(2)
            break
        else:
            print("No, the brackets are not balanced")
            print("\n")
            time.sleep(2)
            break

#Points to grades
def to_grades(points, maxpoints):
    """Calculates the equivalent grade from points scored"""
    while True:
        if points == "" or maxpoints == "":
            print("Nothing to do...")
            points = input("To calculate the grade type in the numbers of points scored.\n")
            maxpoints = input("What is the maximum number of points available?\n")
        elif points.isalpha() or maxpoints.isalpha():
            print("Only numbers allowed, try again!\n")
            points = input("To calculate the grade type in the numbers of points scored.\n")
            maxpoints = input("What is the maximum number of points available?\n")
        else:
            break

    try:
        maxpoints = int(maxpoints)
        points = int(points)

        a = 90 * maxpoints / 100
        b = 80 * maxpoints /100
        c = 70 * maxpoints /100
        d = 60 * maxpoints /100
        e = 55 * maxpoints /100
        fx = 54 * maxpoints /100
        f = 50 * maxpoints /100

        grade = "Your score (" + str(points) + " points) converts to a grade "

        if points >= a:
            grade += "A.  Amazing work!"
        elif points < a and points >= b:
            grade += "B.  Great!"
        elif points < b and points >= c:
            grade += "C.  Overall very good."
        elif points < c and points >= d:
            grade += "D.  Good."
        elif points < d and points >= e:
            grade += "E.  Acceptable."
        elif points <= fx and points > f:
            grade += "Fx. More work is needed before a score can be given."
        elif points <= f:
            grade += "F.  You failed."

        print("\n" + grade + "\n")
        time.sleep(2)

    except ValueError:
        print("\nPlease try again with numbers only!\n")

#Word compare
def word_compare(word1, word2, word3, word4):
    """ Compares the first word, user1, to see if the first word
        starts with the second, includes the third and ends with the fourth word """
    if word1 == "" or word2 == "" or word3 == "" or word4 == "":
        print("\nNothing to do...\n")
        time.sleep(1)
    else:
        test1 = word1.startswith(word2)
        test2 = word1.count(word3)
        test3 = word1.endswith(word4)

        result = test1 and test2 and test3
        if result:
            print("\nYes, there is a match!")
            print("The first word starts with the second word")
            print("includes the third word")
            print("and ends with the fourth word!\n")
            time.sleep(3)
        else:
            print("\nNo match.\n")
            time.sleep(2)
