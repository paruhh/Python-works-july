# print pattern
#111
#222
#333

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


#print pattern
#1 2 3
#1 2 3
#1 2 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()


# print pattern
#kelly kelly kelly
#alan alan alan
#jenny jenny jenny

# l=['kelly','alan','jenny']
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


#print pattern of 2 set
#n=[1,2,3]
#qns=[what,when,why]
#print
#1
# what when why
#2
#what when why
#3
#what when why

# n=[1,2,3]
# qns=['what','when','why']
# for i in n:
#     print(i)
#     for j in qns:
#         print(j,end=" ")
#     print()


# d=[
#     {'id':101,'name':'arun','age':23},
#     {'id':102,'name':'abhi','age':25},
#     {'id':103,'name':'anu','age':24}
# ]
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()

#print patter star
#  *
#  * *
#  * * *
#  * * * *

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# print pattern $
#   $
#   $ $
#   $ $ $
#   $ $ $ $
#   $ $ $ $ $

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('$',end=" ")
#     print()

#print pattern of even nos as
# 2 2 2 2
# 4 4 4 4
# 6 6 6 6
# 8 8 8 8
#
# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

#print pattern as
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

# print pattern as zeros but diagonals like 1234

#   1 0 0 0
#   0 2 0 0
#   0 0 3 0
#   0 0 0 4


# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# print pattern as reverse number
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()



# print pattern as inverted triangle
# * * * *
# * * *
# * *
# *

# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()

# print pattern as continues numbers
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         n+=1
#     print()

# print pattern as

# 1
# 1 0
# 1 0 1
# 1 0 1 0

# for i in range(1,5):
#     for j in range(i):
#         if j%2!=0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()


#print pattern as continues numbers
# 1
# 4 9
# 16 25 36
# 49 64 81 100

# n=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(n**2,end=" ")
#         n+=1
#     print()


#*
#***
#*****
#*******


# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#
#     print()

# print pattern
# 1
# 3 5
# 7 9 11
# 13 15 17 19
# n=1
# for i in range(1,4,2):
#     for j in range(i):
#         print(n,end=" ")
#         n+=2
#     print()
#
# #print patter with alphabets
#
# # A
# # B C
# # D E F
# # G H I J
#
#
# # K=ord('A')
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print(chr(K),end=" ")
# #         K=K+1
# #     print()

#print pattern
# A
# B B
# C C C
# D D D D


# N=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(N),end=" ")
#     N=N+1
#     print()

# print pattren
# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     N=ord('A')
#     for j in range(1,i+1):
#         print(chr(N),end=" ")
#         N=N+1
#     print()