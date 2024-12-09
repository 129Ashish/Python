#tuple methods , indexing and slicing 

my_tuple = (1, 2, 3, 2, 1)
print(my_tuple.count(2))  
print(my_tuple.index(3))  
print()

print("tuple indexing:")
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements using indexing
print(my_tuple[0]) 
print(my_tuple[1])  
print(my_tuple[4]) 

# Accessing elements from the end using negative indexing
print(my_tuple[-1])
print(my_tuple[-2]) 
print()

print("slicing in tuples :")
my_tuple = (10, 20, 30, 40, 50, 60, 70)
print(my_tuple[1:4])   
print(my_tuple[:3]) 
print(my_tuple[4:]) 
print(my_tuple[-3:]) 
print(my_tuple[::2])    
print(my_tuple[1:6:2])

#sets
print("creating set :")
my_set = {1, 2, 3}
another_set = set([4, 5, 6])#using the set constructor
mixed_set = {1, "Hello", 3.14}
print(my_set)   
print(another_set)     
print(mixed_set)     
print()

