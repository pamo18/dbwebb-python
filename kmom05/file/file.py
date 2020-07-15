#!/usr/bin/env python3
"""
file
"""

filename = "items.txt"

with open(filename) as filehandle:
    line = filehandle.readline().strip()

print(line)

items_as_list = line.split(",")

items_as_list.append("cup")

list_as_str = ",".join(items_as_list)

print(items_as_list)
print(list_as_str)

with open(filename, "w") as filehandle:
    filehandle.write(list_as_str)
