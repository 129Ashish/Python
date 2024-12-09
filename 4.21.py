#files read and write operations

#10.python program to perform read and write operations on a file

file1 = open("myfile.txt", "w")
L = ["This is table.... \n", "This is chair ...\n", "This is pencil.... \n"]
file1.write("Hello Hi! from me.... \n")
file1.write("Hello There ...\n")
file1.write("Hello World ....\n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")
print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth byte from the beginning.
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()


file2 =open("myfile2.txt","w")
L2=["We are in class \n","We are in a Lab \n","We are in Python Lab"]
file2.writelines(L2)
file2.close()

file2=open("myfile2.txt","r+")
print("Output from the second file is :")
print(file2.read())
print()
