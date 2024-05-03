from GUI import MainMenu  # Importing the MainMenu class from the GUI module

import tkinter as tk  # Importing the tkinter module 

def main():
    # Create a Tkinter window
    root = tk.Tk()  # Creating an instance of the Tk class to create the main window
    root.title("Main Menu")  # title of the window
    root.geometry("400x300")  # size of the window 
    root.configure(bg="yellow")  #background color of the window to yellow

    # Create the main menu
    main_menu = MainMenu(root)  # Creating an instance of the MainMenu class 

    root.mainloop()  # Tkinter event loop to display the window and handle events

if __name__ == "__main__":
    main()  # Calling the main function 
