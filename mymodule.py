#Create a package named Shapes containing modules circle.py  and
# rectangle.py

#define functions to calculate the area and perimeter of  circle and rectangle.

# write a program mymodule.py to import all these functions from the circle and
# rectangle modules and perform required operations



from Shapes.circle import *
r=float(input("Enter radius of circle: "))
area(r)
perimeter(r)



from Shapes.rectangle import *
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
area(l,b)
perimeter(l,b)


