##  positional argumts   #####

# def fun(n,a):
#     print("Name",n)
#     print("Age",a)
# fun("arun",23)
# fun(23,"arun")

### keyword argument ###

# def fun(n,a):
#     print("Name",n)
#     print("Age",a)
# fun(n="Arun",a=23)
# fun(a=28,n="anu")

## default argument   ###

# def fun(n,a=24):
#     print("Name",n)
#     print("Age",a)
# fun(n="Arun")
# fun(a=28,n="anu")

###    variable length argument  or arbitary argmt  ####

## variable length positional
## we can send multiple no of positional argmts
## here values stored as tuple sequence
# def fun(*args):
#     print("Arbitary positional arguments",args)
# fun(10,20)
# fun(10,20,30)



# define a function to find sum of nos using arbitary positional argmts


def add(*args):
    s=0
    for i in args:
        s=s+i
    print(s)
add(10,20)
add(100,200,300)

#normal code
# def fun(a,b):
#     print(a,b)
# fun(10,20)
# #fun(10,20,30)  ## error here we use variable length argmt

## variable length keyword agmt
## here values stored as dictionary type


# def fun(**kwargs):
#     print("Arbitary variable length keywords",kwargs)
# fun(a=10)
# fun(a=10,b=20)
# fun(a=100,b=200,c=300)