from tkinter import messagebox  # Importing messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format

class Client:
    def __init__(self, client_id=None, name=None, address=None, contact_details=None, budget=None):
        # Constructor for the Client class
        # Initialize client attributes with values 
        self.client_id = client_id  # Unique client ID
        self.name = name  # Name of the client
        self.address = address  # Address of the client
        self.contact_details = contact_details  # Contact details of the client
        self.budget = budget  # Budget allocated for the client

    def add_client(self):
        # Method to add a new client to the file
        # Create a dictionary with client details
        client_data = {
            "client_id": self.client_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "budget": self.budget
        }
        
        # Write client details to a binary file using pickle
        with open("clients.pickle", "ab") as file:  # Use "ab" to append data to the file
            pickle.dump(client_data, file)

    def delete_client(self, client_id):
        # Method to delete a client from the file
        # Load client details from the binary file
        try:
            with open("clients.pickle", "rb") as file:
                clients = pickle.load(file)

            # Check if clients is a list
            if isinstance(clients, dict):
                clients = [clients]

            # Find and remove the client with the given ID
            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    clients.remove(client)
                    break
            else:
                messagebox.showerror("Error", "Client not found!")  # Display error message if client not found
                return

            # Write the updated list of clients back to the file
            with open("clients.pickle", "wb") as file:
                pickle.dump(clients, file)

            messagebox.showinfo("Success", "Client deleted successfully!")  # Display success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")  # Display error message if file not found

    def modify_client(self, client_id, modified_client_details):
        # Method to modify details of an existing client
        # Load clients from the file
        try:
            with open("clients.pickle", "rb") as file:
                clients = pickle.load(file)

            # Check if clients is a list with a single dictionary inside
            if isinstance(clients, dict):
                clients = [clients]

            # Find the client with the given ID and update its details
            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    client.update(modified_client_details)
                    break

            # Save the updated clients back to the file
            with open("clients.pickle", "wb") as file:
                pickle.dump(clients, file)

            messagebox.showinfo("Success", "Client details modified successfully!")  # Display success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")  # Display error message if file not found
    
    @staticmethod
    def display_client_by_id(client_id):
        # Static method to display client details based on the given ID
        # Load client details from the binary file
        try:
            with open("clients.pickle", "rb") as file:
                clients = pickle.load(file)

            if isinstance(clients, dict):
                clients = [clients]

            # Find the client with the given ID
            for client in clients:
                if str(client["client_id"]) == str(client_id):
                    return client

            return None
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")  # Display error message if file not found
            return None
