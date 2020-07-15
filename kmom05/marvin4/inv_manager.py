#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inventory manager using json
"""
import json

filename = "inv.data.txt"
rucksack = []
with open(filename, 'r') as filehandle:
    rucksack = json.load(filehandle)

def inv():
    """
    prints contents of the rucksack
    """
    if not rucksack:
        print("The rucksack is empty!")
    else:
        print("The rucksack has the following: " + str(rucksack))

def inv_save():
    """
    save the rucksack contents to file on quitting
    """
    global rucksack
    with open(filename, 'w') as f:
        json.dump(rucksack, f)

def inv_pick(item):
    """
    puts items in the rucksack
    """
    item = item.replace("inv pick ", "")
    item = str(item)
    global rucksack
    if len(rucksack) <= 4:
        rucksack.append(item)
        print("You have picked up: " + item)
    else:
        print("Sorry, the rucksack is full.")

def inv_drop(item):
    """
    drops item from rucksack
    """
    item = item.replace("inv drop ", "")
    item = str(item)
    global rucksack
    if rucksack:
        if item in rucksack:
            rucksack.remove(item)
            print("You have droped: " + item)
        else:
            print("There is no " + item + " in the rucksack.")
    else:
        print("There is no " + item + " in the rucksack because it is empty!")

def inv_drop_all():
    """
    empty file
    """
    empty = input("This will remove all items from the rucksack, are you sure (y/n)\n")
    if empty == "y":
        global rucksack
        rucksack = []
        print("The rucksack is now empty")
    else:
        print("Cancelled")
