"""
    Name: todo_list_1.py
    Written by: Josiah Andrews
    Written on: 9/14/23
    Purpose: create a list of items for user to keep track of
"""

#TODO: create empty list
user_list = []

#TODO: ask user how many items to add to list and loop that many times
list_length = int(input("How many items do you want to put in the list?\n\t"))

for i in range (0,list_length):
    new_item = input("Enter new item for todo list: ")
    user_list.append(new_item)

#TODO: display user list
print("\nTODO LIST:")
for i in range(0,list_length):
    print(f"{i+1}:\t{user_list[i]}")