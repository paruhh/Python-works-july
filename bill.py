# write a program to calculating current bill based on the following criteria

#criteria
#    units consumed      rates per unit
#       <=100                   zero cost
#        101-200            5RS/unit
#       201-300             10RS/unit
#Above 301 - 15RS/unit
# 325 units
# 0-100 - zero
#101-200 - 100*5
#201-300 - 100*10
#300 above - 25*15

#u=int(input("Enter the unit used : "))
#if (u<=100):
#    bill=0
#elif u>100 and u<=200:
#    bill=0+(u-100)*5
#elif(u>200 and u<=300):
#    bill=0+500+(u-200)*10
#else:
#    bill=0+500+1000+(u-300)*15
#print("The bill amount : ",bill)

#write a program to check whether the user entered number is 2 digit or 3 digit or4 digit

#n=input("Enter a number to check : ")
#if len(n)==2:
#    print(n," is a 2 digit number")
#elif len(n)==3:
#    print(n," is 3 digit number")
#else:
#    print(" number is 4 digit")




#write a basic calculator program to perform arithmetic operations

#n1=int(input("Enter 1st number : "))
#n2=int(input("Enter 2nd number: "))
#op=input("Enter operation : ")
#if op=='+':
#    print("sum is :",n1+n2)
#elif op=='-':
#    print("Difference is : ",n1-n2)
#elif op=='*':
#    print("multiplication is : ",n1*n2)
#elif op=='/':
#    print("Quotient is : ",n1/n2)
#elif op=='%':
#    print("modular is : ",n1%n2)
#elif op=='//':
#    print("floor division : ",n1//n2)
#else:
#    print("Please enter a valid operator")


#write a program to print number of days in a month

#l1=['january','march','may','july','august','october','december']
#l2=['april','june','september','november']
#l3=['february',]
#m=input("Enter the month : ")
#if m in l1:
#    print(f"{m} has 31 days")
#elif m in l2:
#    print(f"{m} has 30 days ")
#else:
#    print(f"{m} has 28 or 29 days")


# write a program to print grades based on the following criteria

#90-100 - grade A
# 81-90 - grade B
# 71 -80 - grade c
#61- 70 - grade D
#below 61 - grade E

mark=int(input("Enter the mark : "))
if mark>=90 and mark<=100:
    print("Grade A")
elif mark>80:
    print("Grade B")
elif mark>70:
    print("Grade C")
elif mark>60:
    print("Grade D")
else:
    print("Grade E")