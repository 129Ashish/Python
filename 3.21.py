#creating dictionaries
#accessing and modifying key values pairs
#del statements

print("creating a dictionary :")
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hello":23
}
my_dict2 = dict(name="Bob", age=25, city="Los Angeles")

print(my_dict)
print(my_dict2)
print()

print("Accessing a dictionary :")
print(my_dict["age"])
print(my_dict["name"])
print(my_dict2["name"])
print()


print("Modifying a dictionary :")
my_dict["age"]=49
my_dict2["name"]="ramanujan"
print(my_dict)
print(my_dict2)
print()

print("using del statement :")
del my_dict["age"]
print(my_dict)
del my_dict2["name"]
print(my_dict2)
print()

print("Iterating dictionary elements")
for key in my_dict:
    print(key,my_dict[key])

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(key,value)
