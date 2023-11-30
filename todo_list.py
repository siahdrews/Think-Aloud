"""
    Name: todo_list.py
    Written by: Josiah Andrews
    Written on: 11/30/23
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
        self.root.iconbitmap("todolist.ico")
        self.create_widgets()
        self.list_widgets()

        # Set the theme to light or dark
        sv_ttk.set_theme("dark")
        # Call the mainloop method to start program
        mainloop()

    # ask user to input items for lists
    def new_items(self, *args):
        # get new item from entry
        self.new_item = self.entry.get()

        # append new item to lsit and update length
        self._user_list.append(self.new_item)
        self.list_length = len(self._user_list)

        # update list widgets
        self.update_widgets()

        # 0 starts the selection at the begining of the entry widget text
        # END finishes the selection at the end of the entry widget text
        self.entry.selection_range(0, END)

    def delete_items(self, index):
        if 0 <= index < len(self._user_list):
            del self._user_list[index]
            self.update_widgets()

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
    
    # TODO: save and quit program
    def quit_program(self):
        # call save_list
        self.save_list()
        #quit program
        sys.exit()

    # TODO: Create list widgets
    def list_widgets(self):
        # CREATE WIDGETS FOR DISPLAYING LIST
        self.list_frame = LabelFrame(
            self.root,
            text="TODO LIST",
            relief=GROOVE
        )
        # creates a label for each for each item in the list, and grids it based on index
        for index, element in enumerate(self._user_list):
            self.label = Label(self.list_frame, text=f"{element}")
            self.label.grid(row=index, column=0, sticky="w")
        
        # grids the frame
        self.list_frame.grid_configure(padx=20, pady=20)

        # updates the widgets so they are with the correct list
        self.update_widgets()
        
        # adds padding to each widget
        for widget in self.list_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
    
    def update_widgets(self):
        # destroy old widgets
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # add new widgets
        for index, element in enumerate(self._user_list):
            self.label = Label(self.list_frame, text=f"{element}")
            self.label.grid(row=index, column=0, sticky="w")

            # create buttons to delete each item
            delete_button = Button(self.list_frame, text="Delete", command=lambda i=index: self.delete_items(i))
            delete_button.grid(row=index, column=1)

        # add padding for new widgets
        for widget in self.list_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    
    #TODO: Create main widgets
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

        self.btn_save = Button(
            self.main_frame,
            text="Save List",
            command=self.save_list
        )

        self.btn_quit = Button(
            self.main_frame,
            text="Quit Program",
            command=self.quit_program
        )


        # GRID WIDGETS-------------------------------------
        self.entry.grid(row=0, column=0)
        self.btn_new_item.grid(row=0, column=1)
        self.btn_save.grid(row=1, column=0)
        self.btn_quit.grid(row=1, column=1)
        

        # Set padding for all widgets inside the frame
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)
        
        

        # Set padding between frame and window
        self.main_frame.grid_configure(padx=20, pady=20)
        
        
        # Start the program with focus on the entry widget
        self.entry.focus_set()

        # Bind both enter key to the convert method
        # when either enter key is pressed,
        # The convert method will be fired
        # <Return> - Enter key on the main keyboard
        # <KP_Enter> - Enter key on the number pad/key pad
        self.root.bind("<Return>", self.new_items)
        self.root.bind("<KP_Enter>", self.new_items)

    
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
    #my_list.display_list()
    my_list.save_list()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
        