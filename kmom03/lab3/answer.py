#!/usr/bin/env python3

"""
33f6c8bda661a92a97816980ca68c336
python
lab3
v3
pamo18
2018-08-26 09:56:54
v3.1.0 (2018-08-17)

Generated 2018-08-26 11:56:55 by dbwebb lab-utility v3.1.0 (2018-08-17).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In these exercises we will work with functions.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function called `greeter` that returns `"Hi, the weather is nice
# today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def greeter():
    """greeter"""
    return "Hi, the weather is nice today!"





ANSWER = greeter()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Assign the words: 'milk' and 'helicopter' to two different variables.
#
# Create a function and pass the two words as arguments to it. Your function
# should return them as a single word.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
wordone = "milk"
wordtwo = "helicopter"

def combine(a, b):
    """combine"""
    return a + b



ANSWER = combine(wordone, wordtwo)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function called `funny_word` that takes one argument and prepends
# it to the string ' is a funny word'. **EXAMPLE:** If the argument is
# 'water', the function should return: `"water is a funny word"`.
#
# Use the argument 'music' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def funny_word(funny):
    """funny_word"""
    return funny + " is a funny word"





ANSWER = funny_word("music")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function called `summation` that takes two arguments. The function
# should return the sum of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 72 and 78.
#
# Write your code below and put the answer into the variable ANSWER.
#
def summation(a, b):
    """summation"""
    return a + b





ANSWER = summation(72, 78)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a function called `multiplication` that takes two arguments. The
# function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 72 and 78.
#
# Write your code below and put the answer into the variable ANSWER.
#
def multiplication(a, b):
    """multiplication"""
    return a * b





ANSWER = multiplication(72, 78)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a function called `in_range` that takes one argument. The function
# should return `True` if the argument is higher than 50 and lower than 100.
# If the number is out of range, the function should return `False`. The
# return type should be boolean.
#
# Use the argument 20 and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def in_range(num):
    """in_range"""
    return bool(num > 50 and num < 100)




ANSWER = in_range(20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a function called `multiplicator`. Inside the function create a loop
# that iterates from 5 to 20 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. The function should return a comma-separated string of the squared
# numbers,  without an ending `,`.
#
# Answer with a call to the function `multiplicator`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplicator(numone, numtwo):
    """multiplicator"""
    result = ""
    for i in range(numone, numtwo+ 1):
        if i < numtwo:
            x = str(multiplication(i, i)) + ","
            result += x
        else:
            x = str(multiplication(i, i))
            result += x
    return result




ANSWER = multiplicator(5, 20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a function called `decider`. The function takes one argument. If the
# argument is a string return a call to `funny_word()`, if the argument is an
# integer return the square of the argument by using the `multiplication`
# function.
#
# Answer with a call to the function `decider` with the value `fartlek` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#

def decider(decide):
    """decider"""
    if isinstance(decide, str):
        return funny_word(decide)
    elif isinstance(decide, int):
        return multiplication(decide, decide)





ANSWER = decider("fartlek")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (1 points)
#
# Create a function called `double_decider`. The function takes two
# arguments. For each argument call the `decider` function. Concatenate the
# returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# hemidemisemiquaver and 93 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#
def double_decider(one, two):
    """double_decider"""
    a = decider(one)
    b = decider(two)
    c = str(a) + ' and the square is ' + str(b)
    return c




ANSWER = double_decider("hemidemisemiquaver", 93)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Create a function that returns a binary string value of a given integer.
# Return only the binary number and not any identification that it is a
# binary number.
#
# Example: Calling the function with the number 3 should return `"11"`.
#
# Answer with a call to the function with the argument 20.
#
# Write your code below and put the answer into the variable ANSWER.
#

def binary(num):
    """binary"""
    x = bin(num)
    return x[2:]



ANSWER = binary(20)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters. The function should return a
# string with the format "Lower case letters: #, upper case letters: #". Only
# count letters, you can ignore space and special characters.
#
# Answer with a call to the function with the argument: `"Pack my Box with
# five dozen LiQuor juGs."`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def sort_letters(words):
    """sort_letters"""
    l = 0
    u = 0
    lower = "Lower case letters: "
    upper = ", upper case letters: "

    for letter in words:
        if letter.isupper():
            u += 1
        elif letter.islower():
            l += 1
        else:
            continue

    return lower + str(l) + upper + str(u)


ANSWER = sort_letters("Pack my Box with five dozen LiQuor juGs.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
