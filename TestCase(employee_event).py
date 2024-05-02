from employee import JobTitle, Employee, Manager
from event import SupplierType, EventType, Client, Guest, Supplier, Venue, Event

# Example for Employees
# Creating employee instances
employee1 = Employee("Susan Meyers", "EMP001", JobTitle.SALES_MANAGER, 37500, 45, "1979-05-15", "AB123456")
employee2 = Employee("Shyam Sundar", "EMP002", JobTitle.SALES_PERSON, 20000, 28, "1996-10-20", "CD789012")
employee3 = Employee("Salma J Sam", "EMP003", JobTitle.SALES_PERSON, 20000, 32, "1992-08-28", "EF345678")
employee4 = Employee("Joy Rogers", "EMP004", JobTitle.MARKETING_MANAGER, 55000, 40, "1984-02-10", "GH901234")
employee5 = Employee("Mariam Khalid", "EMP005", JobTitle.MARKETER, 40000, 35, "1989-11-05", "IJ567890")
employee6 = Employee("Roudha Ahli", "EMP006", JobTitle.ACCOUNTANT, 45000, 38, "1986-07-12", "KL123456")

# Setting managers for employees
employee2.set_manager(employee1)
employee3.set_manager(employee1)
employee5.set_manager(employee4)

# Example for Events
# Creating event instance
event1 = Event("EV001", EventType.WEDDINGS, "Summer Wedding", "2024-06-15", "18:00", 6, "Lake Como", "CLI001", 100000)

# Adding guests to the event
guest1 = Guest("G001", "Damon Salvatore", "456 Oak St", "damon@gmail.com")
guest2 = Guest("G002", "Hind Ahli", "789 Khawaneej St", "hind123@gmail.com")
event1.add_guest(guest1)
event1.add_guest(guest2)

# Adding suppliers to the event
catering_supplier = Supplier("SUP001", "Delicious Caterers", "789 Jumeirah St", "catering@gmail.com", SupplierType.CATERING)
cleaning_supplier = Supplier("SUP002", "Sparkling Cleaners", "101 Wasl St", "cleaning@gmail.com", SupplierType.CLEANING)
event1.add_supplier(SupplierType.CATERING, catering_supplier)
event1.add_supplier(SupplierType.CLEANING, cleaning_supplier)

# Example for Clients
# Creating client instance
client1 = Client("CLI001", "Smith & Co.", "456 Oak St", "smith@outlook.com", 60000)

# Example for Venues
# Creating venue instance
venue1 = Venue("VEN001", "Grand Hall", "Burj Al Arab", "bestvenues@gmail.com", 50, 200)

# Printing information for demonstration
print("--- Employees ---")
print("Employee 1:", employee1.get_name(), "is a", employee1.get_job_title())
print("Employee 2:", employee2.get_name(), "reports to", employee2.get_manager().get_name())
print("Employee 3:", employee3.get_name(), "reports to", employee3.get_manager().get_name())
print("Employee 5:", employee5.get_name(), "reports to", employee5.get_manager().get_name())

print("\n--- Events ---")
print("Event ID:", event1.get_event_id())
print("Event Type:", event1.get_event_type())
print("Guests:", [guest.get_name() for guest in event1.get_guests()])
print("Suppliers:", {str(supplier_type): supplier.get_name() for supplier_type, supplier in event1.get_suppliers().items()})

print("\n--- Clients ---")
print("Client Name:", client1.get_name())
print("Client Budget:", client1.get_budget())

print("\n--- Venues ---")
print("Venue 1 Name:", venue1.get_name())
print("Minimum Guests:", venue1.get_min_guests())
print("Maximum Guests:", venue1.get_max_guests())
