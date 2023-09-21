"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

ok = ["Jack", "Abe", "Habibi", "Big up maan"] # First I created a variable then I a list with 4 elements 
print(ok) # I used the print statement to print the list


"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

ok.append("Big man") # I used append to add a new element
print(ok)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

ok.remove("Big up maan") # I used the remove element to remove a element from my list
print(ok)


"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

ok[1] = "Gabe" # I used the index of the of Abe to change it to Gabe
print(ok)


"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
# I used the append element to add two new elements to my list

ok.append("Xavi")
ok.append("Carlos")
print(ok)


"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

del ok[3] # I used the del element to deleate the 3rd index in my list
print(ok)


"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

ak = ok[:2] # I used the colon and the index to create a new variable equal to the forst 2 items of my list
print(ak)


"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

lok = ["Sam", "Ter", "Tell"] # I created a new list
a = ok + lok # I added the two lists together to extend my list
print(a)