#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main for marvin
"""
import time
import quote
import feelings
import respond
import marvin


"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

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
    print("Ask me for a quote, lunch maybe or just say hi!")

    choice = input("--> ")

    if choice == "q":
        marvin.quit_program()
        break

    elif choice == "1":
        marvin.username()

    elif "citat" in choice or "quote" in choice:
        quote.citat()
        continue

    elif "hello" in choice or "hi" in choice or "hej" in choice or "hey" in choice:
        respond.respond_hello()
        continue

    elif "lunch" in choice or "hungry" in choice or "äta" in choice or "hungrig" in choice:
        user = input("\nVad bra, jag är också hungrig.  Var ska vi äta, på stan eller Lidköping?\n")
        respond.respond_lunch(user)
        continue

    else:
        print("\nThat is not a valid choice. You can only choose from the menu.")
        continue

    input("\nPress enter to continue...")
    print("\n")

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
        print("12) The Dalek Emperor's supprise!")
        print("\nA1) Letter match.")
        print("A2) Balance brackets.")
        print("\nB1) Points to grades.")
        print("B2) Word compare.")

        option = input("--> ")

        if option == "1":
            marvin.back()
            break

        elif option == "2":
            user = input("What is the temperature in Celcius?\n")
            marvin.temp_convert(user)

        elif option == "3":
            user1 = input("What word shoud i multiply?\n")
            user2 = input("How many times should i multiply " +user1 + "?\n")
            marvin.word_multiply(user1, user2)

        elif option == "4":
            user = input("Type a number?\n")
            marvin.amt_avg(user)

        elif option == "5":
            user = input("The staring number is?\n")
            marvin.num_compare(user)

        elif option == "6":
            user = input("What word do you want to spread?\n")
            marvin.letterply(user)

        elif option == "7":
            user = input("What word should i test?\n")
            marvin.isogram(user)

        elif option == "8":
            user = input("What word should i shake?\n")
            marvin.shake(user)

        elif option == "9":
            user1 = input("What is the first word?\n")
            user2 = input("What is the scond word?\n")
            marvin.is_anagram(user1, user2)

        elif option == "10":
            user = input("What should i make an acronym of?\n")
            marvin.acronym(user)

        elif option == "11":
            user = input("What data should i mask?\n")
            marvin.mask(user)

        elif option == "12":
            feelings.respond_feeling()

        elif str.upper(option) == "A1":
            user1 = input("What is the first word?\n")
            user2 = input("What word should i compare with?\n")
            marvin.letter_match(user1, user2)

        elif str.upper(option) == "A2":
            user = input("Type in the combination of brackets to test if they are balanced.\n")
            marvin.balance_test(user)

        elif str.upper(option) == "B1":
            user1 = input("To calculate the grade type in the numbers of points scored.\n")
            user2 = input("What is the maximum number of points available?\n")
            marvin.to_grades(user1, user2)

        elif str.upper(option) == "B2":
            user1 = input("What is the first word to compare with?\n")
            user2 = input("What is the second word?\n")
            user3 = input("What is the third word?\n")
            user4 = input("What is the fourth word?\n")
            marvin.word_compare(user1, user2, user3, user4)

        elif "citat" in option or "quote" in option:
            quote.citat()
            print("\n")
            continue

        elif "hello" in option or "hi" in option or "hej" in option or "hey" in option:
            respond.respond_hello()
            print("\n")
            time.sleep(2)
            continue

        elif "lunch" in option or "hungry" in option or "äta" in option or "hungrig" in option:
            user = input("\nVad bra, jag är också hungrig.  Var ska vi äta, på stan eller Lidköping?\n")
            respond.respond_lunch(user)
            print("\n")
            time.sleep(2)
            continue

        else:
            print("Not an option, choose again!\n")
            time.sleep(1)
