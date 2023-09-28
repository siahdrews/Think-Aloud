"""
    Name: todo_list_2.py
    Written by: Josiah Andrews
    Written on: 9/128/23
    Purpose: create a list of items for user to keep track of
"""
# import to save todo list to downloads folder
from pathlib import Path

class TodoList:
    def __init__(self):
        #TODO: create empty list
        self._user_list = []

    # ask user to input items for lists
    def new_items(self):
        self.new_item = input("Enter new item for todo list: ")
        self._user_list.append(self.new_item)
        self.list_length = len(self._user_list)


    #TODO: display user list
    def display_list(self):
        print("\nTODO LIST:")
        for i in range(0,self.list_length):
            print(f"{i+1}:\t{self._user_list[i]}")
        
    
    #TODO: write todo list to text file
    def save_list(self):
        # define path to save file to downloads folder and name file 'todolist.txt'
        downloads_path = str(Path.home() / "Downloads" / "todolist.txt")
        # set the file name to the downloads path
        self.fileName = downloads_path
        # save file to the downloads folder
        self.todolist = open(self.fileName, 'a') # the 'a' appends new items rather than overwriting them
        for item in self._user_list:
            self.todolist.write(item + "\n")
        self.todolist.close()

# main function
def main():
    my_list = TodoList()
    run_again = "y"
    # menu loop
    while (run_again == "y"):
        my_list.new_items()
        run_again = input("Do you wish to add another item? (Y/N)\n\t>> ").lower()
    my_list.display_list()
    my_list.save_list()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
        