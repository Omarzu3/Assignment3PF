from tkinter import messagebox  # Importing messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format

class Guest:
    def __init__(self, guest_id=None, name=None, address=None, contact_details=None):
        # Constructor for the Guest class
        # Initialize guest attributes 
        self.guest_id = guest_id  # Unique ID for the guest
        self.name = name  # Name of the guest
        self.address = address  # Address of the guest
        self.contact_details = contact_details  # Contact details of the guest

    def add_guest(self):
        # Method to add a new guest to the file
        # Create a dictionary with guest details
        guest_data = {
            "guest_id": self.guest_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details
        }
        
        # Write guest details to a binary file using pickle
        with open("guests.pickle", "ab") as file:  # Use "ab" to append data to the file
            pickle.dump(guest_data, file)

    def delete_guest(self, guest_id):
        # Method to delete a guest from the file
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)

            # Check if guests is a list
            if isinstance(guests, dict):
                guests = [guests]

            # Find and remove the guest with the given ID
            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    guests.remove(guest)
                    break
            else:
                messagebox.showerror("Error", "Guest not found!")
                return

            # Write the updated list of guests back to the file
            with open("guests.pickle", "wb") as file:
                pickle.dump(guests, file)

            messagebox.showinfo("Success", "Guest deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No Guests found!")

    def modify_guest(self, guest_id, modified_guest_details):
        # Method to modify details of an existing guest
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)

            # Check if guests is a list with a single dictionary inside
            if isinstance(guests, dict):
                guests = [guests]

            # Find the guest with the given ID and update its details
            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    guest.update(modified_guest_details)
                    break

            # Save the updated guests back to the file
            with open("guests.pickle", "wb") as file:
                pickle.dump(guests, file)

            messagebox.showinfo("Success", "Guest details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")

    @staticmethod
    def display_guest_by_id(guest_id):
        # Static method to display guest details based on the given ID
        try:
            with open("guests.pickle", "rb") as file:
                guests = pickle.load(file)

            if isinstance(guests, dict):
                guests = [guests]

            # Find the guest with the given ID
            for guest in guests:
                if str(guest["guest_id"]) == str(guest_id):
                    return guest

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")
            return None
