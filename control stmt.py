#string s="python"
#print string s

# s="python"
# for i in s:
#     print(i)

# stop the loop when i='h'

s="python"
# for i in s:
#     if i=='h':
#         break
#     print(i)


#skip the loop when i=='h'

s="python"
# for i in s:
#     if i=='h':
#         continue
#     print(i)


#l=[23,45,12,78,90,51,75] stop the loop when i>50

l=[23,45,12,78,90,51,75]
# for i in l:
#     if i>50:
#         break
#     print(i)


#skip all even nos from the list l

# for i in l:
#     if i%2==0:
#         continue
#     print(i)
#
# print first even number greater than 50

# for i in l:
#     if i%2==0 and i>50:
#         print(i)
#         # break

#count all even nos in the list

# count=0
# for i in l:
#     if i%2==0:
#         count=count+1
# print(count)


#find sum of the list

# sum=0
# for i in l:
#     sum=sum+i
# print(sum)


#find product of odd nos in the list

# product=1
# for i in l:
#     product=product*i
# print(product)


#print nos at even index position

# for i in range(len(l)):
#     if i%2==0:
#         print(l[i])


# find maximum of 2 nos

# n1=int(input("Enter a number: "))
# n2=int(input("Enter 2nd number: "))
# if n1>n2:
#     print(f"{n1},is greater")
# else:
#     print(f"{n2},is greater")
#
# find maximum of 3 nos

# n1=int(input("Enter a number: "))
# n2=int(input("Enter 2nd number: "))
# n3=int(input("Enter 3rd number: "))
# if n1>n2 and n1>n3:
#      print(f"{n1},is greater")
# elif n2>n1 and n2>n3:
#     print(f"{n2},is greater")
# else:
#     print(f"{n3},is greater")


#check whether a number is 3 digit,4 digit or 2 digit

# a=int(input("Enter a number: "))
# if 10<=a<=99:
#     print(f"{a} is 2 digit number")
# elif 100<=a<=999:
#     print(f"{a} is 3 digit number")
# elif 1000<=a<=9999:
#     print(f"{a} is 4 digit number")
# else:
#     print("Number is not 2digit,3digit or 4 digit")




#print each digit in a number

# n=int(input("Enter a number : "))
# s=str(n)
# for i in s:
#     print(i)


#print sum of digits of a number

# sum=0
# n=int(input("Enter a number : "))
# s=str(n)
# for i in s:
#     sum=sum+int(i)
# print(sum)

#print product of digit of numbers

# product=1
# n=int(input("Enter a number : "))
# s=str(n)
# for i in s:
#     product=product*int(i)
# print(product)
