# TASK A : Loop Mastery

# Print numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i)

# Print multiplication table of a number
# n = int(input("Enter a number to print its table:\n"))
# print("Table of ",n,":")
# for i in range(1,11):
#     print(f"{n} x {i} =",i*n)

# # Count digits of a number using loop
# n = int(input("Enter a number:\n"))
# count = 0
# while n!=0:
#     count+=1
#     n//=10
# print("Number of digits in your number:",count)

# Sum of digits of a number
# n = int(input("Enter a number:\n"))
# sum = 0
# while n!=0:
#     ans = n%10
#     sum += ans
#     n //= 10
# print("Sum of digits of your number:",sum)

# Check if a number is Armstrong
# n = int(input("Enter a number:\n"))
# m = n
# o = m
# count = 0
# ans = 0
# while n!=0:
#     count += 1
#     n //= 10
# for i in range(1,count+1):
#     digit = m % 10
#     ans += (digit**count)
#     m //= 10
# if o == ans:
#     print("Its an Armstrong Number.")
# else:
#     print("Not an Armstrong Number.")

# TASK B : Pattern Problems

# *
# **
# ***
# ****
# *****
# n = int(input("Enter a number:\n"))
# i = 1
# while i<=n:
#     j = 1
#     while j<=i:
#         print("*",end = '')
#         j+=1
#     i += 1
#     print(end = '\n')

# *****
# ****
# ***
# **
# *
# n = int(input("Enter a number:\n"))
# i = 1
# while i<=n:
#     j = 1
#     while j<=n-i+1:
#         print("*",end = '')
#         j+=1
#     i += 1
#     print(end = '\n')

# 1
# 12
# 123
# 1234
# n = int(input("Enter a number:\n"))
# i = 1
# while i<=n:
#     j = 1
#     while j<=i:
#         print(j,end = '')
#         j+=1
#     i += 1
#     print(end = '\n')