"""
* The class defines what the object is while the object refers to something unique

* F.eks in the example below the class defines what a student IS. A student have a name, major and a gpa
  - The "self" refers to the object. It relates the class definitions to the object.
  - In the main program we will construct a object that defines WHO the student it. Someone unique.
"""


class Student:
    # The "__init__" is our initializing function. It defines our custom class/data-type
    # This function also runs every time a new instance/object is created. Maybe you want to iterate a number for each
    # - new object 
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # We are also going to define a class function that checks if a student did well based on their gpa
    def did_do_well(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
