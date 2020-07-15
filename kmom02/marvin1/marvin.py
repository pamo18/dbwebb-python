#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import time

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

    choice = input("--> ")

    if choice == "q":
        print("\nExterminate, Exterminate!\n")
        time.sleep(1)
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nThe Dalek Emperor says:\n")
        print("Hello %s - you dont seem to be The Doctor " % name)
        print("Choose your option wisely!")

    else:
        print("That is not a valid choice. You can only choose from the menu.")
        continue

    input("\nPress enter to continue...")
    print("\n")

    while True:
        print("1) Return to start.")
        print("2) Celcius till Farenheit.")
        print("3) Word multiplying.")
        print("4) Amount and average.")
        print("5) Number comparison.")
        print("6) Word virus.")
        print("7) Isogram test.")
        print("\nA1) Letter match.")
        print("A2) Balance brackets.")

        option = input("--> ")

        #Return to start
        if option == "1":
            print("Restarting...")
            time.sleep(1)
            break

        #Celcius till Farenheit
        elif option == "2":
            temp = input("What is the temperature in Celcius?\n")
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
                    temp = input("What is the temperature in Celcius?\n")

        #Word multiplying
        elif option == "3":
            word = input("What word shoud i multiply?\n")
            multiply = input("How many times should i multiply " +word + "?\n")

            if word == "":
                print("Nothing to do...")
            elif multiply == "":
                print("Nothing to do...")
            else:
                while True:
                    try:
                        multiply = int(multiply)
                        print((word + " ") * multiply)
                        print("\n")
                        time.sleep(3)
                        break
                    except ValueError:
                        print("You must type a number!")
                        multiply = input("How many times should i multiply " +word + "?\n")

        #Amount and average
        elif option == "4":
            number = 0
            newnumber = 0
            count = 0
            print("Type 'done' to calculate!")
            print("\n")

            while True:
                try:
                    newnumber = input("Type a number?\n")
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
        elif option == "5":
            lastnumber = 0
            newnumber = 0
            print("Type 'done' to finish!")
            print("\n")

            while True:
                lastnumber = input("The staring number is?\n")
                if lastnumber == "done":
                    break
                else:
                    try:
                        lastnumber = int(lastnumber)
                        break
                    except ValueError:
                        print("Only numbers allowed!")

            while True:
                if lastnumber == "done":
                    print("\n")
                    print("Nothing to do...")
                    print("\n")
                    time.sleep(1)
                    break
                else:
                    newnumber = input("What number should i compare " + str(lastnumber) + " with?\n")
                    print("\n")
                    if newnumber == "done":
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

        #Word virus, each letter multiplies by 1 more than the last letter aba a-bb-aaa-
        elif option == "6":
            while True:
                word = input("What word do you want to spread?\n")
                if word.isalpha():
                    break
                else:
                    print("You must enter a word!")

            count = 1
            virus = ""
            for letter in word:
                virus += letter * count + "-"
                count += 1
            print("\n")
            print(virus)
            print("\n")
            time.sleep(3)

        #Isogram test
        elif option == "7":
            while True:
                isogramtest = input("What word should i test?\n")
                print("\n")
                if isogramtest.isalpha():
                    break
                else:
                    print("You must enter a word!")

            isogram = True
            for letter in isogramtest:
                if isogramtest.count(letter) > 1:
                    isogram = False
                    break

            if isogram:
                print("Yes, '" + isogramtest + "' is an isogram!")
                time.sleep(3)
            else:
                print("No, '" + isogramtest + "' is not an isogram!")
                time.sleep(3)
            print("\n")

        #Letter match, are all the letters of a second word present in the first word
        elif str.upper(option) == "A1":
            while True:
                word1 = input("What is the first word?\n")
                if word1.isalpha():
                    word2 = input("What word should i compare with?\n")
                    if word2.isalpha():
                        break
                    else:
                        print("You must enter a word!")
                else:
                    print("You must enter a word!")
            match = True
            for letter in word2:
                if not word1.count(letter):
                    match = False
                    break

            if match:
                print("Yes, there is a match! All the letters in '" + word2 + "' are present in '" +word1 + "'")
                time.sleep(3)
            else:
                print("No, there is no match!")
                time.sleep(3)
            print("\n")

        #Balance brackets
        elif str.upper(option) == "A2":
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
            opened = "[{("
            closed = "]})"
            balanced = True

            while True:
                retry = False
                while True:
                    bracket_test = input("Type in the combination of brackets to test if they are balanced\n")
                    if bracket_test == "":
                        print("Nothing to do...")
                    else:
                        break

                for bracket in bracket_test:
                    if bracket in opened:
                        s.add(bracket)
                    elif bracket in closed:
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

        else:
            print("Not an option, choose again!\n")
            time.sleep(1)
