#!/usr/bin/env python3

"""
c2626151b62efc302ba956d43efc04ee
python
lab4
v3
pamo18
2018-09-21 09:51:02
v3.1.3 (2018-09-13)

Generated 2018-09-21 11:51:02 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""
import physics as ph
from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'mYsecretPASSW0rd'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def valid_password(password):
    """
    password check
    """
    if len(password) >= 8:
        if any(i.isupper() for i in password):
            if any(i.islower() for i in password):
                return bool(any(i.isdigit() for i in password))

result = valid_password("mYsecretPASSW0rd")


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'mYsecretpassword'.
#
# Write your code below and put the answer into the variable ANSWER.
#
result = valid_password("mYsecretpassword")





ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument.
#
# Answer with the number of vowels in the following text:
#
# 'And finally, that the source of our dissatisfaction lies in our impulsive
# dependency on our reflexive senses rather than logic.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(word):
    """
    vowel check
    """
    counter = 0
    vowel = "aeiouyåäö"
    word = word.lower()
    for v in vowel:
        counter += word.count(v)
    return counter

test = "And finally, that the source of our dissatisfaction lies in our impulsive \
dependency on our reflexive senses rather than logic."
result = number_of_vowels(test)

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value mYsecretPASSW0rd the function should return the
# following string: 'mYsecretPASSW0rd is a valid password and contains 4
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: mYsecretpassw0rd.
#
# Write your code below and put the answer into the variable ANSWER.
#

def analyze_password(password):
    """
    analyze password
    """
    vowels = str(number_of_vowels(password)) + " vowels."
    if valid_password(password):
        valid = password + " is a valid password and contains "
    else:
        valid = password + " is not a valid password and contains "
    return valid + vowels

result = analyze_password("mYsecretpassw0rd")

ANSWER = result
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `physics.py`. Import your new file/module
# in `answer.py` using the import statement: import physics
#
# In your physics module create a function `free_fall` that calculates the
# speed after a free fall without air resistance. The function takes two
# arguments time and initial speed. The inital speed argument should have a
# default value of 0 and it should be possible to call the function only with
# a time argument.
#
# Tip: the formula for calculating the speed of a free fall without air
# resistance is: speed = initial speed + g * time, where g = 9.82.
#
# Answer with a call to the function with time = 7. Round your answer to two
# decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#


result = round(ph.free_fall(7), 2)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Modify your defined function `free_fall` to take another argument `gravity`
# with a default value of 9.82.
#
# Answer with a call to the function with time = 5, an initial speed of 4 and
# a gravity value of 1.62 (gravity on the moon). Round your answer to two
# decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = round(ph.free_fall(5, 4, 1.62), 2)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Kinetic energy describes the energy of an object with a certain mass (m)
# and velocity (v).
#
# Create a function `kinetic_energy` that calculates the amount of kinetic
# energy of an object. The formula for calculating kinetic energy is: energy
# = 0.5 * m * v².
#
# Use your defined function `free_fall` in combination with `kinetic_energy`
# to calculate the kinetic energy of an object with m = 10 after a free fall
# of time = 8 with the default gravity of earth (9.82).
#
# Round the answer to one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = round(ph.kinetic_energy(10, ph.free_fall(8)), 1)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Potential energy is the energy stored in an object by virtue of the objects
# position in a gravitational field. The higher an object is lifted the
# greater the potential energy. The formula for calculating the potential
# energy is: energy = m * g * h, with m being the mass of the object, g the
# gravity and h the height of the object.
#
# When an object falls, all of the potential energy is converted into kinetic
# energy. So it is possible to calculate the height of the fall based on the
# amount of kinetic energy an object has at the end of the fall using the
# following formula: height = kinetic energy / (m * g).
#
# Create a function `height` that calculates the height of a free fall of
# time = 8 for an object with m = 10 and g = 9.82.
#
# Round the answer to one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#


result = round(ph.height(8, 10), 1)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Every point mass attracts every other point mass by a force acting along
# the line intersecting both points. The formula for calculating the force
# between two point masses is the following: force = G * m1*m2 / r². Where G
# = 6.674 * 10⁻¹¹, m1 and m2 is the masses of the two objects and r is
# the distance between the two objects.
#
# Create a function `gravitational_pull` in your physics module that returns
# the force given three arguments m1, m2 and r.
#
# Answer with the returned value from a call to the function with the
# following arguments m1 = 5.972 * 10²⁴, m2 = 10 and r = 100. The
# calculated force is the gravitational pull between the earth and an object
# with a mass of 10kg and 100 meters above the surface of the earth.
#
# Tip: Use the math.pow(x, y) function.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = ph.gravitational_pull(5.972, 10, 100)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Using the already defined functions `height` and `gravitational_pull` to
# calculate the gravitational pull between the earth (m = 5.972 * 10²⁴)
# and an object of m = 10 before a free fall of 9 seconds.
#
# Round the answer to one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = round(ph.gravitational_pull(5.972, 10, ph.height(9, 10)), 1)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Whether a certain year is a leap year depends on a few different rules.
# There is a leap year every year whose number is perfectly divisible by four
# - except for years which are both divisible by 100 and not divisible by
# 400. The second part of the rule effects century years. For example; the
# century years 1600 and 2000 are leap years, but the century years 1700,
# 1800, and 1900 are not.
#
# Create a function `leap_year` that checks whether a certain year is a leap
# year. The function should take one argument.
#
# Then create another function `leap_decider` that takes two arguments:
# `start_year` and `end_year`. The return value from the function should be a
# string containing the years and whether the years are leap years.
#
# Example: With the arguments start_year: 1999 and end_year: 2005, the string
# would be:
#
# 1999 is not a leap year, 2000 is a leap year, 2001 is not a leap year, 2002
# is not a leap year, 2003 is not a leap year, 2004 is a leap year, 2005 is
# not a leap year
#
# Answer with a call to `leap_decider` with the following arguments 2001 and
# 2007.
#
# Write your code below and put the answer into the variable ANSWER.
#

def leap_year(year):
    """
    leap year checker
    """
    isleapyear = True

    if year%4 == 0:
        if year%100 == 0 and year%400 > 0:
            isleapyear = False
    else:
        isleapyear = False

    if isleapyear:
        if str(year)[2:] == 00:
            if year%400 == 0:
                return
            else:
                isleapyear = False

    return isleapyear

def leap_decider(start_year, end_year):
    """
    leap year range
    """
    sentence = ""
    for y in range(start_year, end_year + 1):
        if leap_year(y):
            sentence += str(y) + " is a leap year, "
        else:
            sentence += str(y) + " is not a leap year, "

    sentence = sentence[:-2]
    return sentence

result = leap_decider(2001, 2007)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function `multiplication_table` that returns a multiplication
# table from 1 up to the argument given. As 4 * 3 = 3 * 4 you only need to
# return half of the multiplication table.
#
# Example: With the argument being 3 the returned multiplication table should
# be:
#
# 1
#
# 2 4
#
# 3 6 9
#
# Which is equal to the string '1\n2 4\n3 6 9\n'
#
#
# Answer with a call to the function with the argument 4.
#
# Write your code below and put the answer into the variable ANSWER.
#
def multiplication_table(times):
    """
    times tables
    """
    i = 1
    x = 1
    table = ""
    for _ in range(0, times):
        for y in range(0, i):
            if y == i - 1:
                table += str(i * x)
            else:
                table += str(i * x) + " "
            x += 1
        i += 1
        x = 1
        table += "\n"
    return table

result = multiplication_table(4)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
