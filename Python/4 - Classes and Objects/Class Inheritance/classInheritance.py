# We import the Principal class and its subclass (Teacher class)
from schoolClass import Principal, Teacher

principal = Principal("male", "Leo", "Eagle", "Palm Beach County")
teacher1 = Teacher("female", "Christina", "Hopkins", "Palm Beach County", "English", "2B")


print("The school principal at " + principal.school_district)
print("Name: " + principal.mention_surname() + principal.first_name + " " + principal.last_name)
print("Pay: " + str(principal.monthtly_pay) + "$")
print("\n")
print("The school teacher at " + teacher1.school_district)
print("Name: " + teacher1.mention_surname() + teacher1.first_name + " " + teacher1.last_name)
print("Class: " + teacher1.which_class)
print("Subject: " + teacher1.subject)
print("Pay: " + str(teacher1.monthtly_pay) + "$")
print("\n")

# We can see if a class is inherited from another class of if a object belongs to certain class like this
print("Is Teacher a subclass of Principal?: " + str(issubclass(Teacher, Principal)))
print("Does the teacher1 object/instance belong to the Teacher class?: " + str(isinstance(teacher1, Teacher)))
print("Does the principal object/instance belong to the Teacher class?: " + str(isinstance(principal, Teacher)))

