#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programmet skriver ut en hälsning
"""
year = 2018 # Hårdkodat värde för vilket år det är


#name = input("Skriv ett namn, klicka sen enter: ") # Ber användaren mata in ett namn
#age = input("Skriv en ålder, klicka sen enter: ") # Ber användaren mata in en ålder
#year_born = str(year - int(age)) # Födelseår räknas ut. (2018 - inmatat värde)

#greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + year_born

#print(greeting) # Skriver ut ett sträng värde

height = input("Height over the sea (meter)")
speed = input("Speed (km/h)?")
temp = input("Temperature outside the plane (Celsius)?")

height_feet = str(int(height) * 3.28084)
speed_mph = str(int(speed) * 0.62137)
temp_f = str(int(temp) * 9 / 5 + 32)

print("The height over the sea is " + height_feet + " feet")
print("The speed is " + speed_mph + " mph")
print("The temperature outside the plane is " + temp_f + " Farenheit")
