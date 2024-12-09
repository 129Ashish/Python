#accessing set elements :

#sets are unordered so cannot be accessed from the index

my_set = {1, 2, 3}
for element in my_set:
    print(element) 

#set methods :
"""add(value): Adds an element to the set.
remove(value): Removes a specified element from the set. Raises a KeyError if the element is not found.
discard(value): Removes a specified element from the set, but does not raise an error if the element is not found.
pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
union(other_set): Returns a new set with elements from both sets.
intersection(other_set): Returns a new set with elements common to both sets.
difference(other_set): Returns a new set with elements in the first set but not in the second."""

my_set = {1, 2, 3}
my_set.add(4)
print(my_set) 

my_set.remove(2)
print(my_set)

my_set.add(5)
print(my_set)

my_set.discard(5)  
print(my_set) 