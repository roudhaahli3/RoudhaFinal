import tkinter as tk
from tkinter import messagebox, simpledialog

from Pickle_datamanage import save_data, load_data

class EventManagementSystemGUI:
    def __init__(self, root):
        # Initialize the GUI
        self.root = root
        self.root.title("Event Management System")  # Set window title
        self.root.geometry("400x300")  # Set window size

        # Load data from files
        self.load_data()

        # Create buttons for different entities
        entities = ["Employees", "Events", "Clients", "Guests", "Suppliers", "Venues"]
        for entity in entities:
            # Create a button for each entity
            tk.Button(root, text=entity, command=lambda e=entity: self.show_submenu(e)).pack()

    def load_data(self):
        # Load data from files
        self.employees = load_data("employees.dat")
        self.events = load_data("events.dat")
        self.clients = load_data("clients.dat")
        self.guests = load_data("guests.dat")
        self.suppliers = load_data("suppliers.dat")
        self.venues = load_data("venues.dat")

    def save_data(self):
        # Save data to files
        save_data(self.employees, "employees.dat")
        save_data(self.events, "events.dat")
        save_data(self.clients, "clients.dat")
        save_data(self.guests, "guests.dat")
        save_data(self.suppliers, "suppliers.dat")
        save_data(self.venues, "venues.dat")

    def show_submenu(self, entity):
        # Create a submenu for the selected entity
        submenu_window = tk.Toplevel(self.root)
        submenu_window.title(f"{entity} Menu")  # Set submenu title
        submenu_window.geometry("300x200")  # Set submenu size

        options = ["Add", "Delete", "Modify", "Display"]
        for option in options:
            # Create buttons for options
            tk.Button(submenu_window, text=f"{option} {entity}", command=lambda o=option, e=entity: self.handle_option(o, e)).pack()

    def handle_option(self, option, entity):
        # Handle the chosen option
        if option == "Add":
            self.add_entity(entity)
        elif option == "Delete":
            self.delete_entity(entity)
        elif option == "Modify":
            self.modify_entity(entity)
        elif option == "Display":
            self.display_entity(entity)

    def add_entity(self, entity):
        # Dummy function for adding an entity
        messagebox.showinfo("Message", f"You chose to add a {entity.lower()}.")

    def delete_entity(self, entity):
        # Dummy function for deleting an entity
        messagebox.showinfo("Message", f"You chose to delete a {entity.lower()}.")

    def modify_entity(self, entity):
        # Dummy function for modifying an entity
        messagebox.showinfo("Message", f"You chose to modify a {entity.lower()}.")

    def display_entity(self, entity):
        # Display the details of the selected entity
        id_number = simpledialog.askstring("ID Number", f"Enter {entity.lower()} ID number:")
        if id_number:
            details = self.get_entity_details(entity, id_number)
            if details:
                messagebox.showinfo(f"{entity} Details", details)
            else:
                messagebox.showerror("Error", f"{entity} with ID {id_number} not found.")

    def get_entity_details(self, entity, id_number):
        # Get details of the entity given its ID number
        if entity == "Employees":
            for emp in self.employees:
                if emp.get_employee_id() == id_number:
                    return "Name:" + emp.get_name() + " - Job Title: " + emp.get_job_title().value +  " - Salary: " + str(emp.get_basic_salary()) + " - Age: " + str(emp.get_age()) + " - DOB: " + emp.get_date_of_birth() + " - Passport: " + emp.get_passport_details()
        elif entity == "Events":
            for event in self.events:
                if event.get_event_id() == id_number:
                    return "Event Type:" + event.get_event_type().value + " - Theme: " + event.get_theme() + " - Date: " + event.get_date() + " - Time: " + str(event.get_time()) + " - Duration: " + str(event.get_duration()) + " - Venue Address: " + event.get_venue_address() + " - Client id " + event.get_client_id() + " - Invoice: " + str(event.get_invoie())
        elif entity == "Clients":
            for client in self.clients:
                if client.get_client_id() == id_number:
                    return "Name:" + client.get_name() + " - Address: " + client.get_address() + " - Contact: " + client.get_contact_details() + " - Budget: " + str(client.get_budget())
        elif entity == "Guests":
            for guest in self.guests:
                if guest.get_guest_id() == id_number:
                    return "Name:" + guest.get_name() + " - Address: " + guest.get_address() + " - Contact: " + guest.get_contact_details()
        elif entity == "Suppliers":
            for supplier in self.suppliers:
                if supplier.get_supplier_id() == id_number:
                    return "Name:" + supplier.get_name() + " - Address: " + supplier.get_address() + " - Conatct: " + supplier.get_contact_details() + " - Supplier: " + supplier.get_supplier_type().value
        elif entity == "Venues":
            for venue in self.venues:
                if venue.get_venue_id() == id_number:
                    return "Name:" + venue.get_name() + " - Address: " + venue.get_address() + " - Contact: " + venue.get_contact_details() + " - Min Guests: " + str(venue.get_min_guests()) + " - Max Guests: " + str(venue.get_max_guests())
        return None

root = tk.Tk()
app = EventManagementSystemGUI(root)
root.mainloop()
