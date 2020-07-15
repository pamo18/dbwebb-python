#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import time
import random

marvin_image = r"""
     _n____n__
     /         \---||--<
    /___________\
    _|____|____|_
    _|____|____|_
     |    |    |
    --------------
    | || || || ||\
    | || || || || \++++++++------<
    ===============
    |   |  |  |   |
   (| O | O| O| O |)
   |   |   |   |   |
  (| O | O | O | O |)
   |   |   |   |    |
 (| O |  O | O  | O |)
  |   |    |    |    |
 (| O |  O |  O |  O |)
 ======================
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2P" + chr(27) + "[;M")
    print(marvin_image)
    print("I'm The Dalek Emperor. I know it all. What can i exterminate for you?")
    print("1) Present yourself to The Dalek Emperor.")
    print("q) Quit (Scared!?)")

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

    choice = input("--> ")

    if choice == "q":
        quit_program()
        break

    elif choice == "1":
        username()

    else:
        print("That is not a valid choice. You can only choose from the menu.")
        continue

    input("\nPress enter to continue...")
    print("\n")

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

    while True:
        print("1) Return to start.")
        print("2) Celcius till Farenheit.")
        print("3) Word multiplying.")
        print("4) Amount and average.")
        print("5) Number comparison.")
        print("6) Letterply.")
        print("7) Isogram test.")
        print("8) Word shaker.")
        print("9) Anagram.")
        print("10) Acronym maker.")
        print("11) Data masker.")
        print("\nA1) Letter match.")
        print("A2) Balance brackets.")
        print("\nB1) Points to grades.")
        print("B2) Word compare.")

        option = input("--> ")

        if option == "1":
            back()
            break

        elif option == "2":
            user = input("What is the temperature in Celcius?\n")
            temp_convert(user)

        elif option == "3":
            user1 = input("What word shoud i multiply?\n")
            user2 = input("How many times should i multiply " +user1 + "?\n")
            word_multiply(user1, user2)

        elif option == "4":
            user = input("Type a number?\n")
            amt_avg(user)

        elif option == "5":
            user = input("The staring number is?\n")
            num_compare(user)

        elif option == "6":
            user = input("What word do you want to spread?\n")
            letterply(user)

        elif option == "7":
            user = input("What word should i test?\n")
            isogram(user)

        elif option == "8":
            user = input("What word should i shake?\n")
            shake(user)

        elif option == "9":
            user1 = input("What is the first word?\n")
            user2 = input("What is the scond word?\n")
            is_anagram(user1, user2)

        elif option == "10":
            user = input("What should i make an acronym of?\n")
            acronym(user)

        elif option == "11":
            user = input("What data should i mask?\n")
            mask(user)

        elif str.upper(option) == "A1":
            user1 = input("What is the first word?\n")
            user2 = input("What word should i compare with?\n")
            letter_match(user1, user2)

        elif str.upper(option) == "A2":
            user = input("Type in the combination of brackets to test if they are balanced.\n")
            balance_test(user)

        elif str.upper(option) == "B1":
            user1 = input("To calculate the grade type in the numbers of points scored.\n")
            user2 = input("What is the maximum number of points available?\n")
            to_grades(user1, user2)

        elif str.upper(option) == "B2":
            user1 = input("What is the first word to compare with?\n")
            user2 = input("What is the second word?\n")
            user3 = input("What is the third word?\n")
            user4 = input("What is the fourth word?\n")
            word_compare(user1, user2, user3, user4)

        else:
            print("Not an option, choose again!\n")
            time.sleep(1)
