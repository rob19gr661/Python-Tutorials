"""
* When we inherit from a class we inherit all of the classes attributes and class functions/methods

* It's impotent to note that if we wish to change some data from the inherited class that's unique for our subclass
  then we simply change the value but setting it equal to something else

   - An example could be be pay. So if our parent class (could be principal) had a pay attribute = 1000$,
     then our subclass (teacher) who inherited that pay attribute could change it by setting pay = 500$ f.eks

Further comments:
----------------------------
 * 1) Instead of copy-pasting all the class->object definitions from the parent class we can instead simplify the
      subclass by having the parent class take care of them. This way we only have to link the new class attributes
      to the object.

 * 2) The reason why the method defined in 1) is better is that it makes it easier to handle the program when multiple
      subclasses are created. Method 2) is only relevant when dealing with a single subclass. Don't have to remember all
      the parents.
"""


class Principal:
    monthtly_pay = 1000

    def __init__(self, gender, first_name, last_name, school_district):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.school_district = school_district

    def mention_surname(self):
        if self.gender == "male":
            return "Mr. "
        else:
            return "Miss. "


# The class passed inside the parents indicates the class we want to inherit from
# We define new attributes that are unique to this subclass (subject, pay). Same can be done with methods and so on
class Teacher(Principal):
    monthtly_pay = 500

    def __init__(self, gender, first_name, last_name, school_district, subject, which_class):
        # 1) We pass the attributes to the "Student" class
        super().__init__(gender, first_name, last_name, school_district)
        # 2) Student.__init__(self, name, major) -> The line above can also be done like this

        # We link the new attributes to the object
        self.subject = subject
        self.which_class = which_class
