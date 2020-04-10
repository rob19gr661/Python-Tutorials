"""
The idea for this program is to manually remove duplicates to get a better understanding of how "set's" work

Process:
-------------
1) For each number in the list we use a second list (duplicate_storage) to store the index location of all its
   duplicates including the index location of the current number

2) We then use the number of index locations stored in "duplicate_storage" to remove a duplicate until only 1
   index location is stored. This means that all duplicates of that specific number are removed.

3) In order to maintain the order of the list the self-made V.2 function is used. The -1 passed in the function will
   find the number at the back at list. Thus we keep the first instance of a specific number in the original list,
   thereby insuring that the order is maintained.
"""

my_list = [10, 10, 20, 20, 30, 40, 50, 10, 30, 20, 30, 10]
my_second = my_list.copy()  # For reference

print("Original List: ")
print(str(my_list) + "\n")


# Removing duplicates manually
for numbers in my_list:
    # Store the value of the index "i" if the index location in the list equals a specific number
    # So for each number in the list we store the index location of it and its duplicates in the list below
    duplicate_storage = [i for i in range(len(my_list)) if my_list[i] == numbers]

    # While we have more than 1 index location stored in "duplicate_storage" (meaning that we have duplicates) we
    # - remove a a duplicate of the number we are currently at in the for-loop
    while len(duplicate_storage) > 1:
        my_list.pop(duplicate_storage[-1])  # V.2 Bette version of the function right below. Maintains order of list
        # my_list.remove(numbers)  # Remember that "remove()" removes the first specified number encountered in the list
        duplicate_storage.pop()  # Remember to pop in order to reduce the number of index locations stored!

print("List ordered manually:")
print(my_list)


# The "list" below (second_list) is called a "set". It removes duplicates by default
print("\n")
second_list = set(my_list)
print("List ordered in a set:")
print(second_list)


"""
# Removing duplicates manually - CLEAN
for numbers in my_list:
    duplicate_storage = [i for i in range(len(my_list)) if my_list[i] == numbers]
    while len(duplicate_storage) > 1:
        my_list.remove(numbers)  
        duplicate_storage.pop() 
"""











