#!/usr/bin/env python3
"""
Testar Python

"""
number_of_apples = 9

if number_of_apples > 10:
    print("Du har mer än 10 äpplen")
elif number_of_apples <= 10 and number_of_apples > 5:
    print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
else:
    print("Du har nog varit hungrig och ätit upp dina äpplen")

print("Nu är vi klara med if-satsen")

# skriver ut:
# Du blev snabbt mätt och åt bara upp några av dina äpplen
# Nu är vi klara med if-satsen

type_of_fruit = "päron"
number_of_fruits = 13

if number_of_fruits > 10:
    if type_of_fruit == "äpple":
        print("Du har mer än 10 äpplen")
    else:
        print("Du har mer än 10 frukter")

    print("Nu är vi klara med den inre if-satsen")

print("Nu är vi klara med den yttre if-satsen")

# skriver ut:
# Du har mer än 10 frukter
# Nu är vi klara med den inre if-satsen
# Nu är vi klara med den yttre if-satsen

for i in range(10):
    print(i)

for number_of_apples in range(3, 15):
    if number_of_apples > 10:
        print("Du har mer än 10 äpplen")
    elif number_of_apples <= 10 and number_of_apples > 5:
        print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
    else:
        print("Du har nog varit hungrig och ätit upp dina äpplen")

for _ in range(5):
    print("Python är ett spännande programmeringsspråk")

for letter in "räksmörgås":
    if letter in "åäö":
        print(letter)

while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
    else:
        number_of_apples = int(user_input)
        if number_of_apples > 10:
            print("Du har mer än 10 äpplen")
        elif number_of_apples <= 10 and number_of_apples > 5:
            print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
        else:
            print("Du har nog varit hungrig och ätit upp dina äpplen")

while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
    else:
        try:
            number_of_apples = int(user_input)
        except ValueError:
            print("Oj! Du skrev inte in en siffra.")
            continue

        if number_of_apples > 10:
            print("Du har mer än 10 äpplen")
        elif number_of_apples <= 10 and number_of_apples > 5:
            print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
        else:
            print("Du har nog varit hungrig och ätit upp dina äpplen")
