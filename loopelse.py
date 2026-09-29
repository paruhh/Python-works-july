#for else stmts

#12345
#
# for i in range(1,6):
#     print(i)
# else:
#     print("hello")
#
# for i in range(1,6):
#     if(i==4):
#         break
# else:
#     print("hello")


# check whether a number is prime or not

# n=int(input("Enter a number : "))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
# else:
#     print("number is neither prime nor composite")

#nested loop

# l=[1,2,3,4,5]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#print a inner loop and outer loop


l=[['lion','tiger'],['cat','rat']]
for i in l:
    print("outer loop iteration",i)
    for j in i:
        print(j,end=" ")
    print()

