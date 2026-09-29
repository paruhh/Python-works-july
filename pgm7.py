# swap or interchanging numbers using 3rd variable


a=10
b=5
print("before swapping a= 10 and b= 5")
temp=a   #temp is a 3rd variable to store the 1st value
a=b
b=temp
print("after swapping a = ",a)
print("after swapping b = ",b)


# swap or interchanging numbers without using 3rd variable

a=10
b=20
print("Before swaping a = 10 and b = 20")
a,b=b,a
print("After swaping")
print(a)
print(b)