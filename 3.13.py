#built in functions used in lists 
#list methods

print("built in functions in lists :")
list=[1,2,3,4,5,6,7,8,9,10]
print(len(list))
print(max(list))
print(min(list))
print(sum(list))
print(sorted(list))
print(reversed(list))


print("list methods :")
print(list)
list.append(4)
print(list)
list.append(9)
print(list)
list.extend([1,2])
print(list)
list.insert(0,111)
print(list)
list.remove(111)  #removes the element
print(list)
top=list.pop()
print(top)
print(list)
print(list.index(9))
print(list.count(1))
print(list.count(2))