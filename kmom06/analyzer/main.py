#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main for analyzer program
"""
import menu
import analyzer

while True:
    menu.menu1()
    filename = input("Type the filename you want to analyze?\n")
    if filename == "q":
        break
    textfile = analyzer.openfile(filename)
    if not textfile:
        continue

    menu.menu2(filename)
    while True:
        choice = input("\nPlease choose an option:\n")
        print("\n")
        if choice == "lines":
            print("There are " + str(analyzer.lines_count(filename)) + " lines.")
        elif choice == "words":
            print("There are " + str(analyzer.words_count(filename)) + " words.")
        elif choice == "letters":
            print("There are " + str(analyzer.letters_count(filename)) + " letters")
        elif choice == "word_frequency":
            analyzer.result2(analyzer.word_frequency(filename))
        elif choice == "letter_frequency":
            analyzer.result2(analyzer.letter_frequency(filename))
        elif choice == "all":
            analyzer.analyze_all(filename)
        elif choice == "q":
            exit()
        elif choice == "change":
            break
        else:
            print("Sorry, choice not found")
