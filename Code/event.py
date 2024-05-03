from tkinter import messagebox  # Importing messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format

class Event:
    def __init__(self, event_id=None, event_type=None, theme=None, date=None, time=None, duration=None, venue_address=None, client_id=None, guest_list=None, catering_company=None, cleaning_company=None, decorations_company=None, entertainment_company=None, furniture_company=None, invoice=None):
        # Constructor for the Event class
        # Initialize event attributes 
        self.event_id = event_id  # Unique ID for the event
        self.event_type = event_type  # Type of the event
        self.theme = theme  # Theme of the event
        self.date = date  # Date of the event
        self.time = time  # Time of the event
        self.duration = duration  # Duration of the event
        self.venue_address = venue_address  # Address of the event venue
        self.client_id = client_id  # ID of the client related with the event
        self.guest_list = guest_list  # List of guests attending the event
        self.catering_company = catering_company  # Catering company for the event
        self.cleaning_company = cleaning_company  # Cleaning company for the event
        self.decorations_company = decorations_company  # Decorations company for the event
        self.entertainment_company = entertainment_company  # Entertainment company for the event
        self.furniture_company = furniture_company  # Furniture company for the event
        self.invoice = invoice  # Invoice details for the event

    def add_event(self):
        # Method to add a new event to the file
        # Create a dictionary with event details
        event_data = {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "theme": self.theme,
            "date": self.date,
            "time": self.time,
            "duration": self.duration,
            "venue_address": self.venue_address,
            "client_id": self.client_id,
            "guest_list": self.guest_list,
            "catering_company": self.catering_company,
            "cleaning_company": self.cleaning_company,
            "decorations_company": self.decorations_company,
            "entertainment_company": self.entertainment_company,
            "furniture_company": self.furniture_company,
            "invoice": self.invoice
        }
        
        # Write event details to a binary file using pickle
        with open("events.pickle", "ab") as file:  # Use "ab" to append data to the file
            pickle.dump(event_data, file)

    def delete_event(self,event_id):
        # Method to delete an event from the file
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)

            # Check if events is a dictionary
            if isinstance(events, dict):
                events = [events]

            # Find the event with the given ID
            for event in events:
                if str(event["event_id"]) == str(event_id):
                    events.remove(event)
                    break
            else:
                messagebox.showerror("Error", "Event not found!")
                return

            # Write the updated list of events back to the file
            with open("events.pickle", "wb") as file:
                pickle.dump(events, file)

            messagebox.showinfo("Success", "Event deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
        
    def modify_event(self, event_id, modified_event_details):
        # Method to modify details of an existing event
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)

            # Check if events is a list with a single dictionary inside
            if isinstance(events, dict):
                events = [events]

            # Find the event with the given ID and update its details
            for event in events:
                if str(event["event_id"]) == str(event_id):
                    event.update(modified_event_details)
                    break

            # Save the updated events back to the file
            with open("events.pickle", "wb") as file:
                pickle.dump(events, file)

            messagebox.showinfo("Success", "Event details modified successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")

    @staticmethod
    def display_event_by_id(event_id):
        # Static method to display event details based on the given ID
        try:
            with open("events.pickle", "rb") as file:
                events = pickle.load(file)

            # Check if events is a list with a single dictionary inside
            if isinstance(events, dict):
                events = [events]

            # Find the event with the given ID
            for event in events:
                if str(event["event_id"]) == str(event_id):
                    return event

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
            return None
