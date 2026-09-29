#print space pattern

#        *
#      * *
#    * * *
#  * * * *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  # extra loop for adding space
#         print(end=" ")
#     for j in range(1,i+1):  #loop for printing star
#         print('*',end="   ")# increase space we get triangle shape
#     k=k-2   ## decrement space value by 2 in each line
#     print()
#

#print patter star
#  *
#  * *
#  * * *
#  * * * *
#  * * *
#  * *
#  *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#print pattern
#         *
#       * *
#     * * *
#   * * * *
#     * * *
#       * *
#         *
#
#

# for i in range(1,5):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(4-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#print pattern diamond

#    *
#   * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *

# for i in range(1,5):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(3,0,-1):
#     for j in range(1,5-i):
#         print("",end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#print pattern
#  E
#  DD
#  CCC
#  BBBB
#  AAAAA

# n=ord('E')
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n),end=" ")
#     n=n-1
#     print()

#print pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1

# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#         i=i-1
#     print()


  ###  OR   ####


# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


# print pattern
#  5
#  4 4
#  3 3 3
#  2 2 2 2
#  1 1 1 1 1

# for i in range(5,0,-1):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print()

#print pattern

# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1


for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end=" ")
    print()