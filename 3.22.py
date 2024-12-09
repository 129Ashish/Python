#built in functions used in dictionaries
#dictionaries methods

"""Summary of Dictionary Methods
clear(): Removes all items.
copy(): Returns a shallow copy.
get(key, default): Returns the value for the specified key.
items(): Returns key-value pairs.
keys(): Returns all keys.
values(): Returns all values.
pop(key, default): Removes and returns the value for the specified key.
popitem(): Removes and returns the last inserted key-value pair.
update(other): Updates the dictionary with key-value pairs from another dictionary."""


my_dict={
    "name":"ashish",
    "class":12,
    "roll":18,
    "age":21
}
print("built in functions used in dictionaries :")
new=my_dict.copy()
print(new)
print(my_dict.get("name"))
print(my_dict.get("age"))
age=my_dict.pop("age")
print(age)
print(my_dict)
my_dict.update({"roll":"not assigned"})
print(my_dict)
my_dict2={'name':'ashish'}
value=my_dict2.setdefault('age',34)
print(my_dict2)
item=my_dict2.popitem()
print(item)
print(my_dict2)
print()

print("dictionaries methods :")
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.clear()
print(my_dict)