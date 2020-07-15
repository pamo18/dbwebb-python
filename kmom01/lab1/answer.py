#!/usr/bin/env python3

"""
d6ee921276c3dcc2607694ac5fbae4d7
python
lab1
v3
pamo18
2018-08-21 15:47:22
v3.1.0 (2018-08-17)

Generated 2018-08-21 17:47:22 by dbwebb lab-utility v3.1.0 (2018-08-17).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 66.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_one = 66


ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 98. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 98
result = num_one + num_two

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 71.
#
# Create another variable called `num_four` and give it the value 74.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 71
num_four = 74
result = (num_four - num_three) + result

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = num_one * num_three


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 71.3.
#
# Create another variable called `float_two` and give it the value 38.25.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number.
#
# Write your code below and put the answer into the variable ANSWER.
#

float_one = 71.3
float_two = 38.25
result = round(float_one + float_two, 2)

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result = ((((num_three + num_one) - num_four) * num_two) + float_two) - float_one

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'screen' and 'water' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

word1 = "screen"
word2 = "water"
result = word1 + word2

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'water' with the integer 66, with a space between the
# two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#

number1 = "66"
result = word2 + " " + number1

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 66 with the word 'screen' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 98 and the word 'water' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#

number2 = "98"
word3 = " and "
result = number1 + " " + word1 + word3 + number2 + " " + word2




ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = "30"
actual_number = 5

result = round(int(string_number) / actual_number, 0)

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH have two plugin-hybrid cars. A new car and an old car. The new car has
# a fast charging mode where 80% of the battery can be charged in 30 minutes.
# The remaining 20% of the battery and the entire battery of the old car is
# charged by 5% every 30 minutes.
#
# During fast charging the effect of the charger is 200W and during normal
# charging the effect of the charger is 100W.
#
# The formula for calculating the amount of energy based on effect and time
# is: `energy = effect * time`. To get the amount of energy in kWh the
# formula is `energy = (effect in W * time in hours) / 1000`.
#
# Calculate the total amount of energy used to fully charge the two cars.
# Answer with the amount of energy in kWh.
#
# Write your code below and put the answer into the variable ANSWER.
#
efects_low = 100
effect_fast = 200
new_car_time_slow = 2
new_car_time_fast = 0.5
old_car_time = 20 * 0.5

new_car_slow_energy = efects_low * new_car_time_slow
new_car_fast_energy = effect_fast * new_car_time_fast
old_car_slow_energy = efects_low * old_car_time

total_energy_kwh = (new_car_slow_energy + new_car_fast_energy + old_car_slow_energy) / 1000

ANSWER = total_energy_kwh

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#

peter = "0731415926"
anna = "0727182818"
time_m = 9
hours_year = str((time_m * 52)/60)

result = "Peter calls from " + peter + " " + "to Anna on " + anna + " " + "for " + hours_year + " hours every year."

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
