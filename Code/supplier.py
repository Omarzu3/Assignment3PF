from tkinter import messagebox  # Importing the messagebox module from tkinter for displaying messages
import pickle  # Importing pickle module for storing data in binary file format
class Supplier:
    def __init__(self, supplier_id=None, name=None, address=None, contact_details=None, menu=None, min_guests=None, max_guests=None):
        # Initializing the Supplier class with attributes 
        self.supplier_id = supplier_id #Unique ID
        self.name = name #Name of supplier
        self.address = address  # address of supplier
        self.contact_details = contact_details     # contact details of supplier
        self.menu = menu  # menu
        self.min_guests = min_guests   # min_guests
        self.max_guests = max_guests   # max_guests

    def add_supplier(self):
        # Method to add a new supplier by creating a dictionary with supplier details and writing it to a binary file using pickle
        supplier_data = {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "address": self.address,
            "contact_details": self.contact_details,
            "menu": self.menu,
            "min_guests": self.min_guests,
            "max_guests": self.max_guests
        }
        with open("suppliers.pickle", "ab") as file:  # Open the file in append binary mode
            pickle.dump(supplier_data, file)  # write the data to the file

    def delete_supplier(self, supplier_id):
        # Method to delete a supplier by loading supplier details from the binary file, finding and removing the supplier with the given ID, and updating the file
        try:
            with open("suppliers.pickle", "rb") as file:  # Open the file in read binary mode
                suppliers = pickle.load(file)  # load the data from the file
            if isinstance(suppliers, dict):
                suppliers = [suppliers]
            for supplier in suppliers:  # Iterate through the list of suppliers
                if str(supplier["supplier_id"]) == str(supplier_id):  # Check if the supplier ID matches the given ID
                    suppliers.remove(supplier)  # Remove the supplier from the list
                    break
            else:
                messagebox.showerror("Error", "Supplier not found!")  # Display an error message if the supplier is not found
                return
            with open("suppliers.pickle", "wb") as file:  # Open the file in write binary mode
                pickle.dump(suppliers, file)  # write the updated data to the file
            messagebox.showinfo("Success", "Supplier deleted successfully!")  # Display a success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No Suppliers found!")  # Display an error message if the file is not found

    def modify_supplier(self, supplier_id, modified_supplier_details):
        # Method to modify supplier details by loading suppliers from the file, finding the supplier with the given ID, updating its details, and saving the changes
        try:
            with open("suppliers.pickle", "rb") as file:  # Open the file in read binary mode
                suppliers = pickle.load(file)  # load the data from the file
            if isinstance(suppliers, dict):
                suppliers = [suppliers]
            for supplier in suppliers:  # Iterate through the list of suppliers
                if str(supplier["supplier_id"]) == str(supplier_id):  # Check if the supplier ID matches the given ID
                    supplier.update(modified_supplier_details)  # Update the supplier details
                    break
            with open("suppliers.pickle", "wb") as file:  # Open the file in write binary mode
                pickle.dump(suppliers, file)  # write the updated data to the file
            messagebox.showinfo("Success", "Supplier details modified successfully!")  # Display a success message
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")  # Display an error message if the file is not found

    @staticmethod
    def display_supplier_by_id(supplier_id):
        # Static method to display supplier details by loading them from the binary file, finding the supplier with the given ID, and returning its details
        try:
            with open("suppliers.pickle", "rb") as file:  # Open the file in read binary mode
                suppliers = pickle.load(file)  # load the data from the file
            if isinstance(suppliers, dict):
                suppliers = [suppliers]
            for supplier in suppliers:  # Iterate through the list of suppliers
                if str(supplier["supplier_id"]) == str(supplier_id):  # Check if the supplier ID matches the given ID
                    return supplier  # Return the supplier details
            return None  # Return None if the supplier is not found
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")  # Display an error message if the file is not found
            return None  # Return None if the file is not found
