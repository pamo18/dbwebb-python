#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
str1 = "Hello World in a variable"
print(str1)

# Combine two strings and print them out
str2 = "Hello World!"
str3 = "Its a nice day today!"
print(str2 + " " + str3)

# Combine string and values
a = 40
b = 2
c = a + b
str4 = "Summan är " + str(c) + "."
print(str2 + " " + str4)

#Print out my name

name = "Paul Moreland"


print("My name is" + " " + name)

cricket = r"""
            ."".
               |    |
               |    |
               |    |
               |    |   ____
               |    |-"~    ~"-.
               |    |            \
               |    |             |
               |    |     N.Z.    |
               |    |__..-------------._
               |    |~~---.._________..--~)
               |    | (  .\    /.  )|.--~~
               |    |  \(@))  ((@)/ |
               |____|      .   \    |
                (__)-.    / bm.m)   /
                (__) )-- ( ~--i/  ./
                (__)./ __ "-.__)  "\
              .(_   \   /           `\
            // (_    '----           |`\
           || |(___.-.____..-~      /   \              _
           || ||(__)       |.__  .-"     \            (_)
           || || |   /    /    ~~          \
           || || |  /   /'                  \
           || || |/    /       ..-~~-.      :\
           || ||/     / ~-._.-'       `\._.'  \
           || /      /~//-/              \ _\\~\
           `/  XXXXX/ // /XXXXXXXXXXXXXXX \  \\ \
     XXXXXXXXXXXXX/' // (XXXXXXXXXXXXXXXXXXX\  \\ `\XX
XXXXXXXXXXXXXXXXXX\ \_/ /XXXXXXXXXXXXXXXXXXXXX\  _| |XXX
 XXXXXXXXXXXXXXXXXX\__/XXXXXXXXXXXXXXXXXXXXXXXXX\___/XXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  """

print(cricket)
