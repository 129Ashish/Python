#indexing and slicing in lists 

print("Indexing in lists :")
list=[1,2,3,4,5,6,7,8,9,10]
n=len(list)
print(n)
print("first element is : ",list[0])
print("last element is :",list[-1])
print("middle element is :",list[n//2])

print("slicing in lists :")
print(list[0:n:1])
print(list[0:n:2])
print(list[0:n:2])
print(list[0:n:3])
print(list[0:n:4])
print(list[::-2])
print(list[:-2])

