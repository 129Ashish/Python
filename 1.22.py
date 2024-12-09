#nested if and if-else-if statements :

"""
given grades data :
   A grade : lies between 90 to 100
   B grade : lies between 80 to 90
   C grade : lies between 70 to 80
   D grade : lies between 50 to 70
   E grade : lies between 33 to 50
   F grade : lies between below 33
"""

x= 'y'
while x=='y' :
    
    
    ask=int(input("Enter 1 to use if-elif program and 2 to use nested if statement :"))


    if ask==1 :
      print("program using if-elif statement has begun..")
      mark=int(input("Enter your marks :"))
      if mark<100 and mark>=90 :
        grade='A'
        print("Your grade is :",grade)
      elif mark<90 and mark>=80 :
        grade='B'
        print("Your grade is :",grade)
      elif mark<80 and mark>=70 :
        grade='C'
        print("Your grade is :",grade)
      elif mark<70 and mark>=50 :
        grade='D'
        print("Your grade is :",grade)
      elif mark<50 and mark>=33 :
        grade='E'
        print("Your grade is :",grade)
      elif mark<33 and mark>=0 :
        grade='F'
        print("Your grade is :",grade)
        print("Better Luck Next Time..")
      else :
        print("Please enter the valid marks ..")

    elif ask==2 :
      is_student=input("Are you a student ? (yes/no):")
      if is_student=='yes':
           print("you are eligible for further verification as a eligible student.")
           age=int(input("Enter your age :"))
           if age<=18 and age>10 :
              print("you are eligible for discount in age and sent fot last step verification..")
              grade=input("Enter your grade : (In capitals):")
              if grade=='A' or grade=='B' or grade=='C':
                print("Now you are completely eligible for student merit discount..")
              else :
                print("sorry you are disqualified for the discount offer ")  
           else :
            print("sorry you are not falling in the eligibility criteria of the discount offer.")   
      else :
            print("Sorry you are not a student That's why you are disqualified..")      
    x =input("Enter do you want to continue the program again : (y/n):")


