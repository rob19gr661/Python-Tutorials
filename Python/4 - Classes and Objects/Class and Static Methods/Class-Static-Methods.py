"""
Class Methods:
* While a regular method takes the instance/object as the first argument (self) a classmethod takes the class as the
  first argument (cls)

* For special usecases a classmethod can be used as a alternative constructor for creating instances/objects. For this
  program that special usecase is passing in a string that needs to be parsed (split up) in order to create the object

  - This way the user wont have to parse the string themself but can instead just type out the relevant information
    in a single continuous string.

Static Methods:
* A static method does not pass anything automatically. Neither "self" or "cls". It just works as a normal function.
    - A method should be a static method if "self" or "cls" is not accessed anywhere within the function
"""

# Some needed time functions
import datetime


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod  # This is called a decorator. It changes the functionality of a function.
    def from_string(cls, emp_str):  # "cls" is a naming convention for referring to the class
        first, last, pay = emp_str.split("-")  # We split up the sting based on the "-"
        return cls(first, last, pay)  # Returns the object

    @staticmethod
    def should_i_work_today(day):
        if day.weekday() == 5 or day.weekday() == 6:  # 5 = saturday and 6 = sunday
            return False
        else:
            return True


# Creating an instance/object using a regular method
emp1 = Employee("Julie", "Klark", 7000)
print(emp1.first)

print("\n")

# Creating an instance/object using a classmethod
emp_str_2 = "John-Kent-7000"
new_employee_2 = Employee.from_string(emp_str_2)  # We pass in the string to the function
print(new_employee_2.first)

print("\n")
my_date = datetime.date(2020, 4, 8)
print("Should Julie and John work today?: " + str(Employee.should_i_work_today(my_date)))  # We call the static method
