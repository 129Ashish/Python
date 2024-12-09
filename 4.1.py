"""1.TUPLES AND SETS :
   creating tuples,
   basic tuple operations,
   indexing and slicing in tuples,
   built in functions used on tuples,
   relation between tuples and lists,
   relation between tuples and dictionaries.
"""

# Creating a tuple
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6  # Parentheses are optional

mixed_tuple = (1, "Hello", 3.14)
# Creating a single-element tuple (note the comma)
single_element_tuple = (42,)

print(my_tuple)         
print(mixed_tuple)    
print(single_element_tuple)  
print(another_tuple)
print()

print("accessing element in tuple :")
my_tuple = (10, 20, 30)
print(my_tuple[0])  
print(my_tuple[1]) 