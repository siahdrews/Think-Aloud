"""
    Name: todo_list_5.py
    Written by: Josiah Andrews
    Written on: 11/19/23
    Purpose: create a list of items for user to keep track of
"""
# import to save todo list to downloads folder
from pathlib import Path

# import tkinter
from tkinter import *

# Override tk widgets with themed ttk widgets if available
from tkinter.ttk import *
#pip install sv-ttk
# ipmort sun valley theme
import sv_ttk

#import system
import sys

class TodoList:
    def __init__(self, user_list, download_location):
        #TODO: create empty list
        self._user_list = user_list
        self._download_path = download_location
        self.list_length = len(self._user_list)
        # Create root window
        self.root = Tk()
        self.root.attributes('-topmost', True)
        self.root.title("Todo List")
        self.create_widgets()

        # Set the theme to light or dark
        sv_ttk.set_theme("dark")
        # Call the mainloop method to start program
        mainloop()

    # ask user to input items for lists
    def new_items(self, *args):
        self.new_item = self.entry.get()
        self._user_list.append(self.new_item)
        self.list_length = len(self._user_list)

    def delete_items(self):
        # display list to user
        self.display_list()
        # ask user what item to delete
        item = int(input("What item would you like to remove [Enter # associated with item]: "))
        print(item)
        self.removed_item = self._user_list.pop(item - 1)
        # print removed item
        print(f"Removed item: {self.removed_item}")
        self.list_length = len(self._user_list)


    #TODO: display user list
    def display_list(self):
        print("\nTODO LIST:")
        for i in range(0,self.list_length):
            print(f"{i+1}:\t{self._user_list[i]}")
        
    
    #TODO: write todo list to text file
    def save_list(self):
        # set the file name to the downloads path
        self.fileName = self._download_path
        # save file to the downloads folder
        self.todolist = open(self.fileName, 'w')
        for item in self._user_list:
            self.todolist.write(item + "\n")
        self.todolist.close()
    
    #TODO: Create widgets
    def create_widgets(self):
        """Create and grid widgets"""
        self.main_frame = LabelFrame(
            self.root,
            text="Enter New Item",
            relief=GROOVE
        )

        # Create entry widget in the frame to get input from user
        self.entry = Entry(
            self.main_frame,    # Assign to parent frame
            width=10            # Width in characters
        )

        self.btn_new_item = Button(
            self.main_frame,
            text="Enter",
            command=self.new_items
        )

        self.btn_delete_item = Button(
            self.main_frame,
            text="Delete item",
            command=self.delete_items
        )

        self.btn_display_list = Button(
            self.main_frame,
            text="Display List",
            command=self.display_list
        )

        self.btn_save = Button(
            self.main_frame,
            text="Save List",
            command=self.save_list
        )

        self.btn_quit = Button(
            self.main_frame,
            text="Quit Program",
            command=sys.exit
        )

        # Set padding between frame and window
        self.main_frame.grid_configure(padx=20, pady=20)

        # Set padding for all widgets inside the frame
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
        
        # Start the program with focus on the entry widget
        self.entry.focus_set()

        # Bind both enter key to the convert method
        # when either enter key is pressed,
        # The convert method will be fired
        # <Return> - Enter key on the main keyboard
        # <KP_Enter> - Enter key on the number pad/key pad
        self.root.bind("<Return>", self.new_items)
        self.root.bind("<KP_Enter>", self.new_items)


# menu function
def menu(list=[], still_running='y'):
    # Print menu
    print(" [1] Add item to list")
    print(" [2] Remove item")
    print(" [3] Print List")
    print(" [4] Save List")
    print(" [Enter] Exit program")

    # Convert input to lower case for easier comparison
    menu_choice = input(">> ")

    if menu_choice == "":
        still_running = 'n'

    elif menu_choice == "1":
        list.new_items()
    
    elif menu_choice == "2":
        list.delete_items()
    
    elif menu_choice == "3":
        list.display_list()
    
    elif menu_choice == "4":
        list.save_list()
    
    return still_running

    
# main function
def main():
    # Create tkinter window


    # file location information
    file_location = "Downloads"
    # define path to save file to downloads folder and name file 'todolist.txt'
    downloads_path = str(Path.home() / file_location / "todolist.txt")

    # open list and save to user_list
    # use try/except to make empty list if todolist.txt does not yet exist
    try:
        user_list = []
        with open(downloads_path) as file:
            for line in file:
                line = line.strip()
                user_list.append(line)
    # if file is not found, create empty list
    except FileNotFoundError:
        user_list = []
    
    except Exception as e:
        # Handle any other exception, prit out exception message
        # You can just use this general exception handleing
        print(f"Something went wrong. \n{e}")

    # Create todolist object
    my_list = TodoList(user_list, downloads_path)

    '''run_again = "y"
    # menu loop
    while (run_again == "y"):
        run_again = menu_gui(my_list)'''
    #menu_gui(my_list)
    my_list.display_list()
    my_list.save_list()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
        