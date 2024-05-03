from tkinter import messagebox  # Importing the messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format

class Venue:
    def __init__(self, venue_id=None, name=None, address=None, contact_details=None, min_guests=None, max_guests=None):
        # Initializing the Venue class with attributes for venue details
        self.venue_id = venue_id  # Unique ID for venue
        self.name = name   # name of venue
        self.address = address  # address of venue
        self.contact_details = contact_details   #contact details of venue
        self.min_guests = min_guests   # min guests
        self.max_guests = max_guests   # max guests

    def add_venue(self):
        # Method to add a new venue by creating a dictionary with venue details and writing it to a binary file using pickle
        venue_data = {
            "venue_id": self.venue_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "min_guests": self.min_guests,
            "max_guests": self.max_guests
        }
        with open("venues.pickle", "ab") as file:  # Open the file in append binary mode
            pickle.dump(venue_data, file)  # write the data to the file

    def delete_venue(self, venue_id):
        # Method to delete a venue by loading venue details from the binary file, finding and removing the venue with the given ID, and updating the file
        try:
            with open("venues.pickle", "rb") as file:  # Open the file in read binary mode
                venues = pickle.load(file)  # load the data from the file
            if isinstance(venues, dict):
                venues = [venues]
            for venue in venues:  # Iterate through the list of venues
                if str(venue["venue_id"]) == str(venue_id):  # Check if the venue ID matches the given ID
                    venues.remove(venue)  # Remove the venue from the list
                    break
            else:
                messagebox.showerror("Error", "venue not found!")  # Display an error message if the venue is not found
                return
            with open("venues.pickle", "wb") as file:  # Open the file in write binary mode
                pickle.dump(venues, file)  # write the updated data to the file
            messagebox.showinfo("Success", "venue deleted successfully!")  # Display a success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No venues found!")  # Display an error message if the file is not found

    def modify_venue(self, venue_id, modified_venue_details):
        # Method to modify venue details by loading venues from the file, finding the venue with the given ID, updating its details, and saving the changes
        try:
            with open("venues.pickle", "rb") as file:  # Open the file in read binary mode
                venues = pickle.load(file)  # load the data from the file
            if isinstance(venues, dict):
                venues = [venues]
            for venue in venues:  # Iterate through the list of venues
                if str(venue["venue_id"]) == str(venue_id):  # Check if the venue ID matches the given ID
                    venue.update(modified_venue_details)  # Update the venue details
                    break
            with open("venues.pickle", "wb") as file:  # Open the file in write binary mode
                pickle.dump(venues, file)  # write the updated data to the file
            messagebox.showinfo("Success", "venue details modified successfully!")  # Display a success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No venues found!")  # Display an error message if the file is not found

    @staticmethod
    def display_venue_by_id(venue_id):
        # Static method to display venue details by loading them from the binary file, finding the venue with the given ID, and returning its details
        try:
            with open("venues.pickle", "rb") as file:  # Open the file in read binary mode
                venues = pickle.load(file)  # Deserialize and load the data from the file
            if isinstance(venues, dict):
                venues = [venues]
            for venue in venues:  # Iterate through the list of venues
                if str(venue["venue_id"]) == str(venue_id):  # Check if the venue ID matches the given ID
                    return venue  # Return the venue details
            return None  # Return None if the venue is not found
        except FileNotFoundError:
            messagebox.showerror("Error", "No venues found!")  # Display an error message if the file is not found
            return None  # Return None if the file is not found
