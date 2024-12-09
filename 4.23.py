#reading and writing binary files :

file = open("myfile4.txt", "wb") 
data = bytearray([10, 11, 12, 13])
file.write(data) 
file.close() 

file = open("myfile4.txt", "rb")  
content = file.read()
print("Data read from myfile.txt:", list(content))  
file.close() 