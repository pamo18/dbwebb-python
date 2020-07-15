#!/usr/bin/env python3

"""
ed50e96a55b05f81950c61979b83c41e
python
lab5
v3
pamo18
2018-10-01 08:33:38
v3.1.3 (2018-09-13)

Generated 2018-10-01 10:33:38 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [cougar, flute] and [cougar, Sheen].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1 = ["cougar", "flute"]
list2 = ["cougar", "Sheen"]
list3 = list1 + list2





ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [flute, guitar, drums, piano, bass].
#
# Add the words 'purple' and 'donkey' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list4 = ["flute", "guitar", "drums", "piano", "bass"]
list4.insert(1, "purple")
list4.insert(2, "donkey")


ANSWER = list4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [flute, guitar, drums, piano, bass].
#
# Replace the third word with: 'cord'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list5 = ["flute", "guitar", "drums", "piano", "bass"]
list5[2] = "cord"



ANSWER = list5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [table, wall, desk, chair, floor]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list6 = ["table", "wall", "desk", "chair", "floor"]
s_list6 = sorted(list6, reverse=True)



ANSWER = s_list6

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'floor'
#
# from the list:
#
# > [table, wall, desk, chair, floor]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list7 = ["table", "wall", "desk", "chair", "floor"]

list7.remove("floor")



ANSWER = list7


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

summedlist = sum([67, 50, 2, 39, 15])




ANSWER = summedlist

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [98, 5, 12, 369, 1]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#
list8 = [98, 5, 12, 369, 1]
averagelist8 = sum(list8) / len(list8)





ANSWER = averagelist8

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?grass?is?growing"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#
word = "The?grass?is?growing"
word2 = word.split("?")
word3 = " ".join(word2)





ANSWER = word3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [dvd, mp3, blu-ray, vhs, cd]
#
# and replace the second and third element with
#
# > "green, purple"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list9 = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
list9[1:3] = "green", "purple"





ANSWER = list9

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1 = ["b", "a", "e", "d", "c"]
list2 = ["b", "a", "e", "d", "c"]
result = list1 is list2



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list3 = list1
result = list1 is list3





ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "s"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1[0] = "s"


ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [98, 5, 12, 369, 1]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
def action(inlist):
    """
    action
    """
    outlist = []
    inlist.sort()
    for i in inlist:
        outlist.append(i*10)
    return outlist

result = action([98, 5, 12, 369, 1])


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [98, 5, 12, 369, 1]
#
# as argument.
#
# The function should multiply all even numbers by 1 and add 8 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#
def new_action(new_inlist):
    """
    new new_action
    """
    outlist = []
    for i in new_inlist:
        if i % 2 == 0:
            outlist.append(i)
        else:
            outlist.append(i+8)
    outlist.sort(reverse=True)
    return outlist

result = new_action([98, 5, 12, 369, 1])


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
