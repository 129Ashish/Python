#comments and type conversions, type function and is operator


a=23
b=43
print(a is b)
print(a is not b)

x=2
print(x)
print(type(x))
x=float(x)
print(x)
print(type(x))
x=complex(x)
print(x)
print(type(x))

y="hello world"
y=set(y)
print(y)
print(type(y))
y=tuple(y)
print(y)
print(type(y))
y=list(y)
print(y)
print(type(y))


print("comments are of three types : \n\t\t 1. Single Line comments : '#' \n\t\t 2.Multi-Line Comments ''' \n\t\t 3.Doc -strings ")


# This is a single line comment hash symbol used.
''' This is a multi-line comment  in which single quote is used three times ..
.
..
..
.'''

"""Here this is a doc-string commment in which three double quotes are used simultaneously and can carry any number of content in it which programmer do not want to compiles ."""