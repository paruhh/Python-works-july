### built in functions   ###
      ####  string functions   ####

# write a program to find the position of a specific character in a string

# s="hello world"
# ch="l"
# if ch in s:
#     print("the position of",ch,"is",s.index(ch))
# else:
#     print(ch,"is not present in this string")



# write a program to find the count of a specific character in a string

# s="python coding is fun and easy"
# ch=input("Enter a character: ")
# if ch in s:
#     print("The count of ",ch,"is",s.count(ch))
# else:
#     print(ch,"is not present in this string")




#write a program to create a dictionary where keys are letters and values are the count of each letters

# s="hello word"
# new={}
# for i in s:
#     if i.isalpha():
#         new[i]=s.count(i)
# print(new)

#### number functions  ####

#write a program to create a new list with 5 random 3 digit numbers


# import random
# new=[]
# for i in range(5):
#     new.append(random.randint(100,999))  ## num=random.radint(100,999)
# #                                                 new.append(num)
# print(new)



#write a program to create a 5 digit otp number


# import random
# otp=random.randint(10000,99999)
# print("OTP number is",otp)


#write a program to find the count of letters,space,and digits in a string

# s="python coding is fun and easy  23456"
# letter=0
# space=0
# digit=0
# for i in s:
#     if i.isalpha():
#         letter+=1
#     elif i.isspace():
#         space+=1
#     elif i.isdigit():
#         digit+=1
# print("The count of letters is",letter)
# print("The count of space is",space)
# print("The count of digits is",digit)



#write a program to create a dictionary where keys are words and values are length of the string


# s="python coding is fun and easy"
# new={}
# for i in s.split():
#         new[i]=len(i)
# print(new)

######  list functions   #####


# given a list l=[1,2,3,4,5,5,5,6,1,7] create a new dictionary where keys are numbers and values are count of each number


# l=[1,2,3,4,5,5,5,6,1,7]
# new={}
# for i in l:
#         new[i]=l.count(i)
# print(new)

# given a list l=[34,56,78,32,12,80]
# find the largest element

# l=[34,56,78,32,12,80]
# print(max(l))

#find the second largest element

# l=[34,56,78,32,12,80]
# l.sort()
# print("sorted list",l)
# print("second maximum number : ",l[-2])


# find the smallest element

# l=[34,56,78,32,12,80]
# print(min(l))



#find the second smallest element


# l=[34,56,78,32,12,80]
# l.sort()
# print("sorted list",l)
# print("second minimum number :",l[1])

# given l=[["arun",23,40000],["amal"24,25000],["anu"27,30000]]
#create new list for
# find max salary

# l=[["arun",23,40000],["amal",24,50000],["anu",27,30000]]
# new_salary=[i[2] for i in l ]
# print("salary:",new_salary)
# print(max(new_salary))


    ###  OR     ####

# new=[]
# for i in l:
#     new.append(i[2])
# print(max(new))


# find minimum of age

# new_age=[i[1] for i in l]
# print("age",new_age)
# print(min(new_age))

    #### OR     ####

# age=[]
# for i in l:
#     age.append(i[1])
# print(min(age))


     #### set functions   ####


# l=[1,1,1,2,3,4,4,5]
# remove duplicates from list


# l=[1,1,1,2,3,4,4,5]
# print(set(l))


     ### or   ###

l=[1,1,1,2,3,4,4,5]
new=list(set(l))
print(new)


# remove duplicates without using set()

# l=[1,1,1,2,3,4,4,5]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)


#given 2 lists l1=[23,45,78,90,12,74]   l2=[45,89,23,56,34] print common elements

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# new=[i for i in l1 if i in l2]
# print(new)
#
#        ## or  ##
#
# for i in l1:
#     if i in l2:
#         print(i)


    ## or using intersection by converting it into set  ###

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))

#