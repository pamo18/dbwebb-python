#!/usr/bin/env python3
"""
Lists
"""

shopping = []
print(shopping)
print(type(shopping))

#shopping = ["köttfärs", "krossade tomater", "grädde", "gul lök"]

print(shopping)

#print(dir(shopping))

#help(shopping.append)

shopping.insert(2, "köttfärs")
shopping.insert(0, "grädde")
shopping.insert(1, "krossade tomater")

shopping.append("gul lök")
shopping.append("röd lök")



print(len(shopping))

print(shopping)

remove = shopping.pop(4)


print(remove)

shopping.append("röd lök")
print(shopping)
shopping.remove("röd lök")
print(shopping)

for item in shopping:
    print(item)

for i, item in enumerate(shopping):
    print("{}. {}".format(i + 1, item))
