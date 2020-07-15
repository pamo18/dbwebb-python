#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyzer
"""
import string
def openfile(filename):
    """
    openfile
    """
    try:
        with open(filename):
            return True
    except FileNotFoundError:
        print('File cannot be opened:', filename, '. Try again')
        return False

def lines_count(textfile):
    """
    lines counter
    """
    line_count = 0
    with open(textfile, "r") as filehandle:
        lines = filehandle.readlines()
        for line in lines:
            if not line == "\n":
                line_count += 1
    return line_count

def words_count(textfile):
    """
    word counter
    """
    with open(textfile, "r") as filehandle:
        lines = filehandle.read()
        words = lines.split()
        word_count = len(words)
    return word_count

def letters_count(textfile):
    """
    letter counter
    """
    letter_counter = 0
    with open(textfile, "r") as filehandle:
        lines = filehandle.readlines()
        for line in lines:
            line = line.rstrip()
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            line = line.replace(" ", "")
            letter_counter += len(line)
    return letter_counter

def word_frequency(textfile):
    """
    How often each word occurs
    """
    total_words = words_count(textfile)
    word_counts = dict()
    with open(textfile, "r") as filehandle:
        for line in filehandle:
            line = line.rstrip()
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
        word_list = list()
        for key, val in  word_counts.items():
            word_list.append((val, key))
        word_list.sort(reverse=True)
        topseven = word_list[:7]
        word_freq_result = dict()
        for word in topseven:
            calculated = round((word[0]/int(total_words)*100), 2)
            word_freq_result.update({word[1]:str(calculated)})
        return word_freq_result

def letter_frequency(textfile):
    """
    How often each letter occurs
    """
    total_letters = letters_count(textfile)
    letter_counts = dict()
    letter_freq_result = dict()
    with open(textfile, "r") as filehandle:
        for line in filehandle:
            line = line.rstrip()
            line = line.translate(line.maketrans("", "", string.punctuation))
            line = line.lower()
            line = line.replace(" ", "")
            row = line.split()
            for letters in row:
                for letter in letters:
                    if letter not in letter_counts:
                        letter_counts[letter] = 1
                    else:
                        letter_counts[letter] += 1
        letter_list = list()
        for key, val in letter_counts.items():
            letter_list.append((val, key))
        letter_list.sort(reverse=True)
        topseven = letter_list[:7]
        for letter in topseven:
            calculated = round((letter[0]/int(total_letters)*100), 2)
            letter_freq_result.update({letter[1]:str(calculated)})
        return letter_freq_result

def analyze_all(textfile):
    """
    Returns results for all of the above
    """
    results1 = dict()
    results2 = dict()
    print("In the file " + textfile + " there are:")
    results1.update({"lines" : lines_count(textfile)})
    results1.update({"words" : words_count(textfile)})
    results1.update({"letters" : letters_count(textfile)})
    results2.update(word_frequency(textfile))
    results2.update(letter_frequency(textfile))
    result1(results1)
    result2(results2)

def result1(func):
    """
    Prints results type 1
    """
    for key, val in func.items():
        print(str(val) + " " + key)

def result2(func):
    """
    Prints results type 2
    """
    for key, val in func.items():
        print("'" + key + "'" + " counts for " + val + "%")
