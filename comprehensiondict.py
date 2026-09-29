    ####  dictionary comprehension   ####

#given a list l=[1,2,4,5] create a new dictionary keys are numbers and values are squares of numbers

# l=[1,2,3,4,5]
# new={i:i**2 for i in l}
# print(new)

# create dict with keys are numbers and values are cubes of numbers

# new={i:i**3 for i in l}
# print(new)

#given a list l=[10,20,30,40]
# create a dict where keys are index of numbers and values are numbers

# l=[10,20,30,40]
# new={i:l[i] for i in range(0,len(l))}  ## general format len(l) for the list length
# print(new)


#given a string s='python coding is easy and fun'
#create a new dict where keys are words and values are words length

s="python coding is easy and fun"
new={i:len(i) for i in s.split()}
print(new)