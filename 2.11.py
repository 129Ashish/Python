#all about functions in python 
import random
import math
import datetime

guess=input("Do you want an number : (y/n:)")
x=random.randint(0,100)
print("This is a random number :",x)
root=math.sqrt(x)
print("Square root of the guess number is:",root)
print("This is date and time :",datetime.datetime.now())

def func1():
    print("it is a null parameter function")
def func2(name):
    print("hello",name)
def func3(name="Ramanujan"):
    print("Wassup",name)


func1()
func2("Ashish")
func3()
func3("uttapam")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
print("Addition of two number is :",add(a,b))
print("Subtraction of two number is :",sub(a,b))
print("Multiplication of two number is :",mul(a,b))
print("Division of two number is :",div(a,b))
