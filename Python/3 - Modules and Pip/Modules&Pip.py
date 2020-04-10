"""
Modules & Pip
* A module is a imported Python file that might contain useful functions or pre-defined variables
  - These modules can also be found online

* An easy way to install modules is though "Pip". Pip is a program used to easily install and uninstall
  Python modules, it's basically a file manager

* Let's try to import and use a function defined in another file
"""

import TestModule

input_one = input("Please enter the first number: ")
input_two = input("Please enter the second number you wish to add to the first: ")

# The dot operator used below allows us to access the functions or variables defined in our test module (TestModule)
return_value = TestModule.addition(input_one, input_two)
print("The result of " + str(input_one) + "+" + str(input_two) + " is: " + str(return_value))
