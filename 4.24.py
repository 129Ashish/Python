#in a csv file :

import csv

with open("myfile.csv","w",newline="")as file :
     writer=csv.writer(file)
     data=[10,11,12,13]
     writer.writerow(data)
     file.close()
     

with open("myfile.csv","r")as file :
     reader=csv.reader(file)
     content=list(reader)
print(content)