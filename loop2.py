# #print hello using for loop
#
# s='hello'
# for i in s:
#     print(i)
#
# # print list=[1,2,3,4,5,6]
#
# l=[1,2,3,4,5,6]
# for i in l:
#     print(i)

#print d={'name':'anu','age':20,'course':'python'}

# d={'name':'anu','age':20,'course':'python'}
# for i in d:
#     print(i)

#print even nos in this set s={1,2,3,4,5}

# s={1,2,3,4,5}
# for i in s:
#     if i%2==0:
#         print(i)
#
#print each element in the tuple t=(12,34,65,98,56)

# t=(12,34,65,98,56)
# for i in t:
#     print(i)

#print sum of numbers in list l=[56,89,34,10]

# l=[56,89,34,10]
# s=0
# for i in l:
#     s=s+i
# print(s)

#print each colors in the list colors=['red','green','yellow','blue']

# colors=['red','green','yellow','blue']
# for i in colors:
#     print(i)

# #print keys and values separate d={'a':10,'b':20,'c':30}

# d={'a':10,'b':20,'c':30}
# for i in d:
#     print(i) # print keys only
# for i in d:
#     print(i,":",d[i])#print key and value as pairs
# print(d.values())


#print range of values

# range(1,3,5,7.......17,19)

# for i in range(1,20,2):
#     print(i,end=" ")

# range[8,7,6,5,4,3,2,1]

# for i in range(8,0,-1):
#     print(i,end=" ")

# range(10,8,6,4,2)

# for i in range(10,0,-2)
#     print(i,end=" ")

#range(0,1,2......9,10)

#for i in range(11): #stopping value 11
#     print(i,end=" ")


# Reverse string using slicing

# s="hello"
# print(s[::-1])

# Reverse string without using slicing

# s="hello"
# rev=""
# for i in s:
# #    rev=rev+i # for printing correct order
#     rev=i+rev #printing in reverse order
# print(rev)


#write a program to find a string is palindrome or not

# s=input("Enter the string: ")
# rev=""
# for i in s:
#     rev=i+rev
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#write a program to find a number is palindrome or not

# n=int(input("Enter the number: "))
# rev=0
# temp=n
# for i in range(len(str(n))):
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if temp==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# write a program to reverse a number

# n=int(input("Enter a number : "))
# rev=""
# s=str(n)
# for i in s:
#     rev=i+rev
# print(rev)

## here a list is given find answers of the below qns
## l=[12,34,56,45,89,16,69,33]

# print each no in the list

l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)
# # print even values from the list

#print those numbers which are divisible by '5'

# for i in l:
#     if i%5==0:
#         print(i)
# print those numbers that contain digit '3'

# for i in l:
#     if '3' in str(i):
#         print(i)

# print sum of digits of the  list

# s=0
# for i in l:
#     s=s+i
# print(s)

# print count of even nos in the list

# count=0
# for i in l:
#     if i%2==0:
#         count+=1
# print(count)

# print product of the list

# product=1
# for i in l:
#     product=product*i
# print(product)

# print squares of each number in the given list

# for i in l:
#     print(i**2)

# here is the another list n=[12,4.5,6.8,30,'abhi','hello']

#print float values from the list n

n=[12,4.5,6.8,30,'abhi','hello']
# for i in n:
#     if type(i)==float:
#         print(i)

#print string values from the list n

# for i in n:
#     if type(i)==str:
#         print(i)


#print numbers from the list n

# for i in n:
#     if type(i)==int:
#         print(i)

# print even numbers from the dict d={'a':23,'b':25,'c':28,'d':30,'e':22}

# d={'a':23,'b':25,'c':28,'d':30,'e':22}
# for i in d:
#     if d[i]%2==0:
#         print(d[i])


## here is another list colors=['red','green','blue','orange','yellow','black']
# print the list

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     print(i)
#

#print the starting letter of the list elements

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     print(i[0])



#print colors contain letter 'b'
# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if (i[0]=='b'):
#         print(i)

# print last letter of each color

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     print(i[-1])

#print colors starting with letter 'g'

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if(i[0]=='g'):
#         print(i)

#print first color starting with letter 'b'

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if(i[0]=='b'):
#         print(i)
#         break


#print color end with letter 'e'

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if(i[-1]=='e'):
#         print(i)


#print all colors except color starting with 'b'

# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if(i[0]=='b'):
#         continue
#     print(i)


#print numbers from 100 to 200

# for i in range(100,201):
#     print(i)


#print range of nos 1...5

# for i in range(1,6):
#     print(i)

#print 1,3,5,7,9,11

# for i in range(1,12,2):
#     print(i)

#print 2,4,6,8

# for i in range(2,9,2):
#     print(i)

#print even nos from the list
# l=[23,65,42,80,56,41]
# for i in l:
#     if i%2==0:
#         print(i)

# print prime nos from this list
# l=[23,65,42,80,56,41]
#
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# print all prime nos range 1-100

# for i in range(1,101):
#     if i>1:
#
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

#print all amstrong nos range from 100-1000
#
# for i in range(100,1001):
#     s=str(i)
#     l=len(s)
#     sum=0
#     for j in s:
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)