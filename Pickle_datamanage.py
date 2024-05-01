import pickle

from employee import JobTitle, Employee, Manager
from event import SupplierType, EventType, Client, Guest, Supplier, Venue, Event

def save_data(entities, filename):
    # Save entities to a binary file
    with open(filename, 'wb') as file:
        pickle.dump(entities, file)

# I will add the example data here, so it can be easily accessed in the GUI
# Example data
employees = [
    Employee("Susan Meyers", "EMP001", JobTitle.SALES_MANAGER, 50000, 45, "1979-05-15", "AB123456"),
    Employee("Shyam Sundar", "EMP002", JobTitle.SALES_PERSON, 30000, 28, "1996-10-20", "CD789012"),
    Employee("Salma J Sam", "EMP003", JobTitle.SALES_PERSON, 30000, 32, "1992-08-28", "EF345678"),
    Employee("Joy Rogers", "EMP004", JobTitle.MARKETING_MANAGER, 55000, 40, "1984-02-10", "GH901234"),
    Employee("Mariam Khalid", "EMP005", JobTitle.MARKETER, 40000, 35, "1989-11-05", "IJ567890"),
    Employee("John Doe", "EMP006", JobTitle.ACCOUNTANT, 45000, 38, "1986-07-12", "KL123456")
]

events = [
    Event("EV001", EventType.WEDDINGS, "Classic Wedding", "2024-06-15", "18:00", 6, "123 Main St", "CLI001", "INV001")
]

clients = [
    Client("CLI001", "Smith & Co.", "456 Oak St", "smith@example.com", 20000)
]

guests = [
    Guest("G001", "John Smith", "456 Oak St", "john@example.com"),
    Guest("G002", "Alice Johnson", "789 Elm St", "alice@example.com")
]

suppliers = [
    Supplier("SUP001", "Delicious Caterers", "789 Maple St", "catering@example.com", SupplierType.CATERING),
    Supplier("SUP002", "Sparkling Cleaners", "101 Pine St", "cleaning@example.com", SupplierType.CLEANING)
]

venues = [
    Venue("VEN001", "Grand Hall", "123 Main St", "venue@example.com", 50, 200)
]

# Saving data to files
save_data(employees, "employees.dat")
save_data(events, "events.dat")
save_data(clients, "clients.dat")
save_data(guests, "guests.dat")
save_data(suppliers, "suppliers.dat")
save_data(venues, "venues.dat")

def load_data(filename):
    # Load entities from a binary file
    try:
        with open(filename, 'rb') as file:
            entities = pickle.load(file)
    except FileNotFoundError:
        entities = []
    return entities
