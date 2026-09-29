# # # Q1.Define a function that takes 2 numbers and returns their product

# def product(n1,n2):
#     p=n1*n2
#     return p
# n1=int(input("Enter 1st number: "))
# n2=int(input("Enter 2nd number: "))
# a=product(n1,n2)
# print("product is:",a)


# # Q2.Define a function that takes a string and returns number of vowels
#
# def vowel(s):
#     count=0
#     for i in s:
#         if i in 'aeiouAEIOU':
#             count=count+1
#     return count
# s=input("Enter the string")
# a=vowel(s)
# print("vowels are",a)


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

# def area(l,b):
#     a=l*b
#     return a
# l=int(input("Enter the length: "))
# b=int(input("Enter the breadth: "))
# c=area(l,b)
# print("Area=",c)



# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]


# def even(l):
#     new=[i for i in l if i%2==0]
#     return new
# l=[45,78,90,12,35]
# a=even(l)
# print("Even numbers are:",a)


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
#
# def digits(l):
#     new=[]
#     for i in l:
#         a=i//100
#         b=(i//10)%10
#         c=i%10
#         new.append(a+b+c)
#     return(new)
# l=[123, 345, 111, 678, 134, 809]
# s=digits(l)
# print("sum of digits:",s)


#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]

# def unique(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new+=[i]
#     return new
# l=[12,34,78,12,67,34,90,23]
# a=unique(l)
# print("unique elements:",a)


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]


def common(list1,list2):
    new=[]
    for i in list1:
        if i in list2:
            new+=[i]
    return new
list1=[12,34,56,78,90]
list2=[90,34,11,57,45]
a=common(list1,list2)
print("Common elements:",a)
