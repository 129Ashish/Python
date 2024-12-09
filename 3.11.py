#creating list and list operations
#del statements


empty_list=[]
int_list=[1,2,3,4,5,1,2]
mixed_list=[1,"hey",2.3]
nested_list=[[1,2],["ashish","raman"],[2.2,1.2],[3,4,5,5]]

print("Empty list is :",empty_list)
print("Integer list is :",int_list)
print("Mixed list is :",mixed_list)
print("Nested list is :",nested_list)

print("Accessing list elements:")
list=[1,2,3,4,5]
print(list[1],list[0],list[-1])

print("Modifying list elements :")
list[1]=99
list[-2]=11
print(list)

print("adding elements to a list :")
print(list)
list.append(4)
print(list)
list.extend([22,222,2222])
print(list)
list.insert(0,44) #(index,element)
print(list)


print("the del statement")
print("before  del statement",list)
del list[2]
print(list)
del list[-1]
print(list)