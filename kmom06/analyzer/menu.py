#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
menu for analyzer program
"""

def menu1():
    """
    First menu
    """
    menu = ("\nChoose in the menu below\n", "'q' to quit the program", "change: Change text file\n")
    for item in menu:
        print(item)

def menu2(filename):
    """
    Main menu
    """
    menu = ("\nFile to analyze: " + filename, "\nMenu", "lines: Analyze the number of rows",
            "words: Analyze the number of words",
            "letters: Analyze the number of letters",
            "word_frequency: Analyze the word frequency",
            "letter_frequency: Analyze the letter frequency",
            "all: Analyze " + str(filename) + "\n",
            "'q' to quit the program",
            "change: Change text file\n")
    for item in menu:
        print(item)
