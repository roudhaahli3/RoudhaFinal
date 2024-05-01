from enum import Enum

class SupplierType(Enum):
    '''class to represent the different types of the supplier companies'''
    CATERING = "Catering"
    CLEANING = "Cleaning"
    DECORATIONS = "Decorations"
    ENTERTAINMENT = "Entertainment"
    FURNITURE = "Furniture"

class EventType(Enum):
    '''class to represent the 4 events the organization hosts'''
    WEDDINGS = "Weddings"
    BIRTHDAYS = "Birthdays"
    THEMED_PARTIES = "Themed Parties"
    GRADUATIONS = "Graduations"


class Client:
    '''class to represent a Client'''
   # Initializing the constructor
    def __init__(self, client_id, name, address, contact_details, budget):
        # all attributes are protected
        self._client_id = client_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._budget = budget

    # Getter and setter methods for client_id
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contact_details
    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    # Getter and setter methods for budget
    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = budget


class Guest:
    '''class to represent a guest'''
    # Initializing the constructor
    def __init__(self, guest_id, name, address, contact_details):
        # all attributes are protected
        self._guest_id = guest_id
        self._name = name
        self._address = address
        self._contact_details = contact_details

    # Getter and setter methods for guest_id
    def get_guest_id(self):
        return self._guest_id

    def set_guest_id(self, guest_id):
        self._guest_id = guest_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contact_details
    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details


class Supplier:
    '''class to represent a supplier'''
    # Initializing the constructor
    def __init__(self, supplier_id, name, address, contact_details, supplier_type):
        # all attributes are protected
        self._supplier_id = supplier_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._supplier_type = supplier_type

    # Getter and setter methods for supplier_id
    def get_supplier_id(self):
        return self._supplier_id

    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contact_details
    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    # Getter and setter methods for supplier_type
    def get_supplier_type(self):
        return self._supplier_type

    def set_supplier_type(self, supplier_type):
        self._supplier_type = supplier_type


class Venue:
    '''class to represent the venue'''
    # Initializing the constructor
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        # all attributes are protected
        self._venue_id = venue_id
        self._name = name
        self._address = address
        self._contact_details = contact_details
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Getter and setter methods for venue_id
    def get_venue_id(self):
        return self._venue_id

    def set_venue_id(self, venue_id):
        self._venue_id = venue_id

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Getter and setter methods for contact_details
    def get_contact_details(self):
        return self._contact_details

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    # Getter and setter methods for min_guests
    def get_min_guests(self):
        return self._min_guests

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests

    # Getter and setter methods for max_guests
    def get_max_guests(self):
        return self._max_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests


class Event:
    '''class to represent the Event'''
    # Initializing the attributes
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, invoice):
        # all attributes are protected
        self._event_id = event_id
        self._event_type = event_type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venue_address = venue_address
        self._client_id = client_id
        self._invoice = invoice
        self._guests = []
        self._suppliers = {}

    def add_guest(self, guest):
        self._guests.append(guest)

    def add_supplier(self, supplier_type, supplier):
        self._suppliers[supplier_type] = supplier

    # Getter and setter methods for event_id
    def get_event_id(self):
        return self._event_id

    def set_event_id(self, event_id):
        self._event_id = event_id

    # Getter and setter methods for event_type
    def get_event_type(self):
        return self._event_type

    def set_event_type(self, event_type):
        self._event_type = event_type

    # Getter and setter methods for theme
    def get_theme(self):
        return self._theme

    def set_theme(self, theme):
        self._theme = theme

    # Getter and setter methods for date
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    # Getter and setter methods for time
    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    # Getter and setter methods for duration
    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    # Getter and setter methods for venue_address
    def get_venue_address(self):
        return self._venue_address

    def set_venue_address(self, venue_address):
        self._venue_address = venue_address

    # Getter and setter methods for client_id
    def get_client_id(self):
        return self._client_id

    def set_client_id(self, client_id):
        self._client_id = client_id

    # Getter and setter methods for client_id
    def get_invoie(self):
        return self._invoice

    def set_invoice(self, invoice):
        self._invoice = invoice

    # Getter and setter methods for guests
    def get_guests(self):
        return self._guests

    def set_guests(self, guests):
        self._guests = guests

    # Getter and setter methods for suppliers
    def get_suppliers(self):
        return self._suppliers

    def set_suppliers(self, suppliers):
        self._suppliers = suppliers