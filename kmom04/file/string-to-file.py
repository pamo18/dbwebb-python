#!/usr/bin/env python3
"""
string-to-file
"""

filename = "items.txt"

def menu():
    """
    menu
    """
    print(
        """
1. Show file content
2. Add item, append
3. Replace content
4. Remove an item
        """
        )
    return int(input("Choice: "))

def choice(inp):
    """
    Choice
    """
    if inp == 1:
        print(readfile())
    elif inp == 2:
        write_to_file("\n" + input("Item to add:"), "a")
    elif inp == 3:
        replace_content()
    elif inp == 4:
        remove_item()
    else:
        exit()

def readfile():
    """
    read file
    """
    with open(filename) as filehandle:
        content = filehandle.read()
    return content

def write_to_file(content, mode):
    """
    write to file
    """
    with open(filename, mode) as filehandle:
        filehandle.write(content)

def replace_content():
    """
    replace item
    """
    item = ""
    result = ""
    while item != "q":
        result += item + "\n"
        item = input("Item to add: ")
    write_to_file(result.strip(), "w")

def remove_item():
    """
    remove item
    """
    content = readfile()
    remove = input("What item should be removed: ")
    if remove in content: # check if item to remove exists
        found = content[:content.find(remove)+len(remove)+1]
        keep_pos = len(content[:content.find(remove)+ len(remove)])
        keep_str = content[keep_pos+1:]

        if content[keep_pos] == "\n" and content[keep_pos-(len(remove)+1)] == "\n":
            modified_content = found.replace(remove + "\n", "")
            remaining_content = modified_content + keep_str
        else:
            print(content[keep_pos])
            modified_content = found.replace(remove, "")
            remaining_content = modified_content + keep_str

    write_to_file(remaining_content.strip(), "w")

if __name__ == "__main__":
    while(True):
        choice(menu())
