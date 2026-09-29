#write a program to find greatest of 3 numbers


a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd  number : "))
c=int(input("Enter 3rd number : "))
if a>b and a>c:
    print(a," is greater")
elif b>a and b>c:
    print(b," is greater")
else:
    print(c," is greater")


