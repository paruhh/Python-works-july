#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese



#weight=float(input("Enter the weight : "))
#height=float(input("Enter the height : "))
#bmi=weight/(height**2)
#if bmi<=18.4:
#    print("Status : Underweight")
#elif bmi>=18.5 and bmi<=24.9:
#    print("Status : Normal")
#elif bmi>=25.0 and bmi<=39.9:
#    print("Status : Overweight")
#else:
#    print("Obese")

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.


# p=int(input("Enter product code : "))
# a=float(input("Enter the order amount : "))
# if p==1:
    #if a>1000:
#         discount=(a-(a*10)/100)
#     else:
#         discount=0
# elif p==2:
#     if a>100:
#         discount=(a-(a*5)/100)
#     else:
#         discount=0
# elif p==3:
#     if a>500:
#         discount=(a-(a*10)/100)
#     else:
#         discount=0
# else:
#     print("Enter correct product code ")
# netamount=a-discount
# print("Discount : ",discount)
# print("Net Amount : ",netamount)

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number


#n=int(input("Enter a number to check divisible by 3 or 5 : "))
#if n%3==0 and n%5==0:
#    print("FizzBuzz")
#elif n%3==0:
#    print("Fizz")
#elif n%5==0:
#    print("Buzz")
#else:
#    print(n)