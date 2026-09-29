#GLOBAL  - can access from inside and outside

x=20
print("OUTSIDE",x)


def f():
    print("INSIDE",x)  ##
f()


#LOCAL

def s():
    x=500
    print("inside",x)  ## can access through function
s()
print("outside",x)    ## local variable cannot accessed by outside the fun

## NONLOCAL
def outer():
    x=20   ## non local
    def inner():
        y=30    ##local
        print("Inside inner function",x)
    inner()
    print("Inside Outer Function",x)
outer()

##  LEGB Rule


#BUILT IN




