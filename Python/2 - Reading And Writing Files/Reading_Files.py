"""
Reading from files:
* If you have a folder with the file you wish to edit in the same folder was your python file you can just type
  in the name of the file. Otherwise you should type in the full file-path in the "open" function

* To manipulate a file we use the "open()" function. It takes 2 parameters.
  1. Parameter: File name,
  2. Parameter: Operation - "r" = read, "w" = overwrite, a = append r+ = read & write
"""

#  Lets open up a file to edit and store it in a variable we can manipulate with functions
TestFile = open("Testtest.txt", "r")

print(TestFile.readable())  # Will test if the file is readable. Returns bool
# print(TestFile.read())  # Will print out everything in the file
# print(TestFile.readline())  # Will read and print the first element in the file
print(TestFile.readlines()[1])  # Will take each line and put them into a list. Which line to print can be specified [?]

TestFile.close()  # Good practice to close it again
