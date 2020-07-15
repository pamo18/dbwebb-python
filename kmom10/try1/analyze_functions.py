#!/usr/bin/env python3
"""
Exam module
"""

def spaces(textfile):
    """
    spaces
    """
    count = 0
    with open(textfile, "r") as filehandle:
        for lines in filehandle:
            lines = lines.strip("\n")
            for letter in lines:
                if letter == " ":
                    count += 1
    return count

def letters(textfile):
    """
    spaces
    """
    count = 0
    with open(textfile, "r") as filehandle:
        for lines in filehandle:
            lines = lines.strip("\n")
            lines = lines.lower()
            for letter in lines:
                if letter.isalpha():
                    count += 1
    return count

def specials(textfile):
    """
    spaces
    """
    para = []
    counter = []
    with open(textfile, "r") as filehandle:
        specialchars = [":", ",", ".", "-"]
        for lines in filehandle:
            lines = lines.strip("\n\n")
            para.append(lines)
        for lines in para:
            hits = 0
            for special in specialchars:
                hits += lines.count(special)
            counter.append(hits)

    counter = sorted(counter, reverse=True)[0]

    return counter
