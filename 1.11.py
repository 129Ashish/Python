#operators 


print("there are 7 types of operators in Python :")
print("1.Arithmetic operators \n2.Assignment Operators \n3.Comparison operators \n4.Logical operators \n5.Identity Operators \n6.Membership Operators \n7.Bitwise Operators")


x=10
y=3
print("1.Arithmetic operators :")
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print('modulus',x%y)
print('exponent',x**y)
print("floor division",x//y)

x=4
print("2.Assignment operators :")
print(x)
x=x+4
print(x)
x=x|4
print("or",x)
x=x^4
print("bitwise xor",x)

print("3.Comparison operators :")
x=5
y=7
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


print("4.Logical operators :")
print(x>4 and x<10)
print(x>4 or x<10)
print(not(x>4 and x<10))

print("5.identity operators :")
print(x is y)
print(x is not y )


print("6.membership operators  :")
x=(1)
y=(0,1,2,3,4,5,6,7,8,9)
print(x in y)
print(x not in y)

print("7.bitwise operators :")
x=4
y=2
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<2)
print(x>>2)