from enum import Enum

class JobTitle(Enum):
    '''class to represent the ENUM for the different types of employees'''
    SALES_MANAGER = "Sales Manager"
    SALES_PERSON = "Sales Person"
    MARKETING_MANAGER = "Marketing Manager"
    MARKETER = "Marketer"
    ACCOUNTANT = "Accountant"
    DESIGNER = "Designer"
    HANDYMAN = "Handyman"

class Employee:
    '''class to represent an Employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, job_title, basic_salary, age, date_of_birth, passport_details, manager=None):
        # all attributes are protected
        self._name = name
        self._employee_id = employee_id
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._date_of_birth = date_of_birth
        self._passport_details = passport_details
        self._manager = manager

    # Getter and setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and setter methods for employee_id
    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    # Getter and setter methods for job_title
    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    # Getter and setter methods for basic_salary
    def get_basic_salary(self):
        return self._basic_salary

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    # Getter and setter methods for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and setter methods for date_of_birth
    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    # Getter and setter methods for passport_details
    def get_passport_details(self):
        return self._passport_details

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details

    # Getter and setter methods for manager
    def get_manager(self):
        return self._manager

    def set_manager(self, manager):
        self._manager = manager

class Manager(Employee):
    '''class to represent a Manager that inherits from Employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, job_title, basic_salary, age, date_of_birth, passport_details,
                 managed_employees=None):
        # Initialize the attributes of the parent class
        super().__init__(name, employee_id, job_title, basic_salary, age, date_of_birth, passport_details)
        self._managed_employees = managed_employees

    # Getter and setter methods for managed_employees
    def get_managed_employees(self):
        return self._managed_employees

    def set_managed_employees(self, managed_employees):
        self._managed_employees = managed_employees








