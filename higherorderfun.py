    ###  map type   ####

# create a new list from the existing list  using maping

# l=[1,2,3,4]
# print(set(map(lambda x:x**2,l)))
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
#
#
# # create a new list of cubes
#
# n=[1,2,3,4,5]
# print(list(map(lambda a:a**3,n)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda a:a**0.5,l)))
#
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda a:len(a),colors)))
#
# #create a new list of first characters
#
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda a:a[0],colors)))
#
#
# #create a new list of last characters
#
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda a:a[-1],colors)))
#
# #create a new list of reverse of each elemnt
#
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda a:a[::-1],colors)))
#
#
# #Given a list l=[23,78,12,56]
# #Add 10 to each element in the given sequence
#
# l=[23,78,12,56]
# print(list(map(lambda x:x+10,l)))
#
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
#
# print(list(map(lambda x:x['email'],l)))
#
#


           ### filter type  ###


#create a list of even nos using filter function from the given list

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

     # with map  ##

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x%2==0,l)))


#given a list l=[23,65,89,12,20,33,85,40]
# filter elements greater than 50

l=[23,65,89,12,20,33,85,40]
print(list(filter(lambda x:x>50,l)))

# filter even nos less than 50

l=[23,65,89,12,20,33,85,40]
print(list(filter(lambda x:x%2==0 and x<50,l)))

#given a list fruits=['apple','orange','pineapple','grapes','avacado']
#filter elements whose length greater than 5

fruits=['apple','orange','pineapple','grapes','avacado']
print(list(filter(lambda x:len(x)>5,fruits)))


        #### reduce function    ####

# sum of list
l=[1,2,3,4,5,6]
import functools
print(functools.reduce(lambda a,b:a+b,l,0))

# product of list

l=[1,2,3,4]
import functools
print(functools.reduce(lambda a,b:a*b,l,1))

