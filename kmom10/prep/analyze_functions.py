#!/usr/bin/env python3
"""
Exam module
"""

def vokaler(textfile):
    """
    vokaler
    """
    vokalers = "aeiouy"
    vokaler_count = 0
    with open(textfile, "r") as filehandle:
        for line in filehandle:
            line = line.lower()
            for letters in line:
                for letter in letters:
                    if letter in vokalers:
                        vokaler_count += 1
    return(vokaler_count)

def punkter(textfile):
    """
    punkter
    """
    punkter_count = 0
    with open(textfile, "r") as filehandle:
        for line in filehandle:
            for letter in line:
                if letter == ".":
                    punkter_count += 1
    return(punkter_count)

def bigletters(textfile):
    """
    bigletters
    """
    bigLetterCount = 0
    with open(textfile, "r") as filehandle:
        for line in filehandle:
            for letter in line:
                if letter.isupper():
                    bigLetterCount += 1
    return(bigLetterCount)
