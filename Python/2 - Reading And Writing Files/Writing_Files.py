"""
Writing Files:
"""

# Testing the "a" operation
"""
Test_file = open("Testtest.txt", "a")  # Remember that append will add something to the end of the file

Test_file.write("\nToby - Official poopscooper")  # We add the typed line to the end of the document

Test_file.close()
"""

# Testing the "w" operation 
# Remember that "w" will overwrite the entire file if the same filename is used
# A entirely new file can be created by simply changing the filename in the "open()" function
Test_file = open("Testtest.txt", "w")

Test_file.write("\nToby - Official poopscooper")  # The typed line will be the only thing in the overwritten file

Test_file.close()