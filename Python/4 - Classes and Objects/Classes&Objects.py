"""
Classes and Objects:
* Helps us structure our program
* Allows us to define our own data-types when basic variables lacks the detail
  - Not everything can be represented by basic variables

* Our program will construct two object based on the class defined in the "TestClass.py". For this example the two
  objects will be students. After the object have been constructed the information related to each student will be
  printed
"""
# We import our class
from TestClass import Student
#                   name          major         gpa
student1 = Student("Polle", "Advanced Kissing", 8.0)  # This is our object based on our class
student2 = Student("Lena", "Unconventional Pig Farming", 2.0)

# The dot operator is used to access the class definitions
print("Student name: " + student1.name)
print("Student major: " + student1.major)
print("Student gpa: " + str(student1.gpa))
print("Did the student do well?: " + str(student1.did_do_well())) # We call the class function
print("\n")
print("Student name: " + student2.name)
print("Student major: " + student2.major)
print("Student gpa: " + str(student2.gpa))
print("Did the student do well?: " + str(student2.did_do_well()))
