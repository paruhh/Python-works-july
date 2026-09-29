# write a function for adding 2 numbers

# def add():
#     "sum of two numbers"
#     n1=int(input("Enter 1st number : "))
#     n2=int(input("Enter 2nd number : "))
#     s=n1+n2
#     print("sum =",s)
#     return
# add()

#define a function to display "hello your name"

# def name():
#     n=input("Enter your name : ")
#     print("hello",n)
#     return
# name()

#define a function to find the count of a specific character in a string
#
# def length():
#     count=0
#     s=input("Enter the string: ")
#     ch=input("Enter the character in string: ")
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# length()


#define a function to find the factorial of a number

# def fact():
#     n=int(input("Enter a number : "))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#
#     print("factorial:",f)
#     return
# fact()

#define a function to check whether a number is amstrong or not

# def chk_amstrong():
#     n=int(input("Enter a number :"))
#     sum=0
#     s=str(n)
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#         print("amstrong number")
#     else:
#         print("Not amstrong")
#         return
# chk_amstrong()


# define a function to check whether a number is prime or not

# def prime():
#     n=int(input("Enter a number : "))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("Number is not prime")
#                 break
#         else:
#             print("Number is prime")
#             return
# prime()

#sum of digits of a number using function

# def digits():
#     n=int(input("Enter a number : "))
#     s=0
#     while n>0:
#         d=n%10
#         s=s+d
#         n=n//10
#     print("sum of digits :",s)
#     return
# digits()


## # 18.Write a program to find reverse of a number using function

# def num_rev():
#     n=int(input("Enter the number to reverse : "))
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     print("reverse is:",rev)
#     return
# num_rev()
#



#write a program to find a string is palindrome or not using function

# def palin_str():
#     s=input("Enter the string : ")
#     rev=""
#     for i in s:
#         rev=i+rev
#     if s==rev:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palin_str()


#write a program to find a number is palindrome or not using function

# def palin_num():
#     n=int(input("Enter the number: "))
#     rev=0
#     temp=n
#     for i in range(len(str(n))):
#         d=n%10
#         rev=rev*10+d
#         n=n//10
#     if temp==rev:
#         print("palindrome")
#     else:
#          print("not palindrome")
# palin_num()

# define a function to find the factors of a number

# def factors():
#     n=int(input("Enter the number :"))
#     for i in range(1,n+1):
#         if n%i==0:
#             print("factors:",i)
# factors()


### FUNCTION ARGUMENTS AND PARAMETERS  ####

# write a function to find sum of two nos passing parameters

# def add(a,b):
#     c=a+b
#     print("sum=",c)
#     return
# n1=int(input("Enter 1st no: "))
# n2=int(input("Enter 2nd no: "))
# add(n1,n2)
# #add(5,10)

## write a program to find simple interest

# def simple_intrst(p,n,r):
#     si=(p*n*r)/100
#     print("simple intrest = ",si)
# p=int(input("Enter the principal amount: "))
# n=int(input("Enter the years: "))
# r=int(input("Enter the rate: "))
# simple_intrst(p,n,r)

#define a function that takes string and a character as arguments and print the count of a character in the string


# def length(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# s=input("Enter the string: ")
# ch=input("Enter the character in string: ")
# length(s,ch)


###   RETURN VALUE   ####

# def add(n1,n2):
#     s=n1+n2
#     return s   ### it returns the sum to a
# a=add(10,5)
# print('Sum=',a)

# define a function that takes 3 nos and return the product as result call the function and print the result

# def pdt(a,b,c):
#     p=a*b*c
#     return p
# a=int(input("Enter the 1st no: "))
# b=int(input("Enter the 2nd no: "))
# c=int(input("Enter the 3rd no: "))
# d=pdt(a,b,c)
# print("Product=",d)

# define a function that takes string as arguments and return a new dictionary where keys are words and values are length of each word.
#call the fun and print dict

#s="python coding is easy and fun"

#
# def word():
#     s ="python coding is easy and fun"
#     new = {i: len(i) for i in s.split()}
#     print("new dict",new)
#     return
# word()

### or  ###

# s ="python coding is easy and fun"
# def word(s):
#     new={}
#     for i in s.split():
#         print(i)
#         new[i]=len(i)
#     return new
# a=word(s)
# print(a)


### using normal code create a dict in this way##


# s ="python coding is easy and fun"
# new={}
# for i in s.split():
#     print(i)
#     new[i]=len(i)
# print(new)


#define a function that takes a list of numbers as argument and print the count of even numbers,
# odd numbers and numbers whose value greater than 50 l=[23,56,12,78,98,89,31,67]



# def count_num(l):
#     odd=0
#     even=0
#     greater=0
#     for i in l:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#         if i>50:
#             greater+=1
#     print("count of even numbers",even)
#     print("count of odd numbers",odd)
#     print("count of numbers greater than 50",greater)
# l=[23,56,12,78,98,89,31,67]
# count_num(l)

#define a function that take length of the given list l=["red","green","orange","yellow","blue"]

# def word(l):
#     new=[]
#     for i in l:
#         new.append(len(i))
#     return(new)
# l=["red","green","orange","yellow","blue"]
# a=word(l)
# print(a)
















