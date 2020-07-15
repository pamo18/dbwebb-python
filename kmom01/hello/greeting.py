#!/usr/bin/env python3

"""
Programmet skriver ut en hälsning till Jack Black
"""
year = 2018 # Hårdkodat värde för vilket år det är


name = input("Skriv ett namn, klicka sen enter: ") # Ber användaren mata in ett namn
age = input("Skriv en ålder, klicka sen enter: ") # Ber användaren mata in en ålder
year_born = str(year - int(age)) # Födelseår räknas ut. (2018 - inmatat värde)

greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + year_born

print(greeting) # Skriver ut ett sträng värde
