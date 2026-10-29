# count divisible by 5
# count=0
# for i in range(1,51):
#     if(i%5==0):
#         count+=1
# print("count: ",count)

# sum of odd number
# sum=0
# for i in range(1,21):
#     if(i%2!=0):
#         sum+=i
# print("sum of odd number: ",sum)

# no. divisible by 3 not by 2
# for i in range(1,31):
#     if i%3==0 and i%2!=0:
#      print(i) 

# count positive and negative
# count_pos=0
# count_neg=0
# num=[1,-2,3,-4,5,-6,7,-8,9]
# for i in num:
#    if(i>0):
#       count_pos+=1
#    elif(i<0):
#       count_neg+=1
#    else:
#       print("invalid")
# print("count_pos: ",count_pos)
# print("count_neg: ",count_neg)

# largest number without using max of
# num=[1,20,3067,40,36,57]
# largest=num[0]
# for i in num:
#     if i>largest:
#         largest=i
# print("largest number: ",largest)
        
# factorial
# n=int(input())
# factorial=1
# for i in range(1,n+1):
#      factorial*=i
# print("factorial: ",factorial)

# prime numberr
# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
        
# sum of digit
# n=int(input("enter no.: "))
# digit=0
# sum=0
# while n>0:
#      digit =n%10
#      sum+=digit
#      n=n//10
# print("sum of four digit: ",sum)
 
# armstrong
# n=int(input())
# sum=0
# a=str(n)
# length=len(a)
# for i in a:
#      sum+=int(i)**length
# if sum==n:
#     print("it is armstrong")
# else:  
#   print("it is not armstong") 

# automorpic
# n=int(input())
# sum=0
# for i in str(n):
#     sum+=((n*n)%(10**len(str(n))))
# if sum==n:
#     print("it is automophoric")
# else:
#     print("its not automophic")

# NEON NUMBER
# n=int(input())
# sqr=n*n     #given numb square
# digit_sum=0     #store the squred numb
# for digit in str(sqr):#csnge to str
#     digit_sum+=int(digit)
# if digit_sum==n:
#     print("it is neon")
# else:
#     print("it is not neon")

# perfect number
# num = int(input("Enter a number: "))

# if num <= 0:
#     print(f"{num} is not a Perfect Number.")
# else:
#     divisor_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisor_sum += i

#     if divisor_sum == num:
#         print(f"{num} is a Perfect Number.")
# else:
#  print(f"{num} is not a Perfect Number.")

# peterson number
# num = int(input("Enter a number: "))
# fact_sum = 0
# for i in str(num):
#     digit = int(i)
#     fact = 1        # Calculate factorial of the digit
#     for i in range(1, digit + 1):
#         fact *= i
#     fact_sum += fact
# if fact_sum == num:
#     print(f"{num} is a Peterson Number.")
# else:
#     print(f"{num} is not a Peterson Number.")

# duck number
# num_str = input("Enter a number: ").strip()
# if num_str[0] == '0':
#     print(f"{num_str} is NOT a Duck Number (starts with 0).")
# elif '0' in num_str[1:]:
#     print(f"{num_str} is a Duck Number.")
# else:
#     print(f"{num_str} is NOT a Duck Number (no zero found).")

# num=int(input("enter:"))
# digit_sum=0
# for i in str(num):
#     fact=int(i)
#     digit=1
#     for i in range(1,fact+1):
#         digit*=i
#         digit_sum==digit
#     if digit==num:
#         print("it is peterson")
#     else:
#         print("it is not peterson")
# strong number
# import math
# num=int(input())
# digit_factorial=0
# for digit in str(num):
#     digit_factorial+=math.factorial(int(digit))
# if digit_factorial==num:
#     print("it is strong number")
# else:
#    print("it is not strong number")

# count divisible by 5
# count=0
# for i in range(1,51):
#     if(i%5==0):
#         count+=1
# print("count: ",count)

# sum of odd number
# sum=0
# for i in range(1,21):
#     if(i%2!=0):
#         sum+=i
# print("sum of odd number: ",sum)

# no. divisible by 3 not by 2
# for i in range(1,31):
#     if i%3==0 and i%2!=0:
#      print(i) 

# count positive and negative
# count_pos=0
# count_neg=0
# num=[1,-2,3,-4,5,-6,7,-8,9]
# for i in num:
#    if(i>0):
#       count_pos+=1
#    elif(i<0):
#       count_neg+=1
#    else:
#       print("invalid")
# print("count_pos: ",count_pos)
# print("count_neg: ",count_neg)

# largest number without using max of
# num=[1,20,3067,40,36,57]
# largest=num[0]
# for i in num:
#     if i>largest:
#         largest=i
# print("largest number: ",largest)
        
# factorial
# n=int(input())
# factorial=1
# for i in range(1,n+1):
#      factorial*=i
# print("factorial: ",factorial)

# prime numberr
# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
        
# sum of digit
# n=int(input("enter no.: "))
# digit=0
# sum=0
# while n>0:
#      digit =n%10
#      sum+=digit
#      n=n//10
# print("sum of four digit: ",sum)
 
# armstrong
# n=int(input())
# sum=0
# a=str(n)
# length=len(a)
# for i in a:
#      sum+=int(i)**length
# if sum==n:
#     print("it is armstrong")
# else:  
#   print("it is not armstong") 

# automorpic
# n=int(input())
# sum=0
# for i in str(n):
#     sum+=((n*n)%(10**len(str(n))))
# if sum==n:
#     print("it is automophoric")
# else:
#     print("its not automophic")

# NEON NUMBER
# n=int(input())
# sqr=n*n     #given numb square
# digit_sum=0     #store the squred numb
# for digit in str(sqr):#csnge to str
#     digit_sum+=int(digit)
# if digit_sum==n:
#     print("it is neon")
# else:
#     print("it is not neon")

# perfect number
# num = int(input("Enter a number: "))

# if num <= 0:
#     print(f"{num} is not a Perfect Number.")
# else:
#     divisor_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisor_sum += i

#     if divisor_sum == num:
#         print(f"{num} is a Perfect Number.")
# else:
#  print(f"{num} is not a Perfect Number.")

# peterson number
# num = int(input("Enter a number: "))
# fact_sum = 0
# for i in str(num):
#     digit = int(i)
#     fact = 1        # Calculate factorial of the digit
#     for i in range(1, digit + 1):
#         fact *= i
#     fact_sum += fact
# if fact_sum == num:
#     print(f"{num} is a Peterson Number.")
# else:
#     print(f"{num} is not a Peterson Number.")

# duck number
# num_str = input("Enter a number: ").strip()
# if num_str[0] == '0':
#     print(f"{num_str} is NOT a Duck Number (starts with 0).")
# elif '0' in num_str[1:]:
#     print(f"{num_str} is a Duck Number.")
# else:
#     print(f"{num_str} is NOT a Duck Number (no zero found).")

# num=int(input("enter:"))
# digit_sum=0
# for i in str(num):
#     fact=int(i)
#     digit=1
#     for i in range(1,fact+1):
#         digit*=i
#         digit_sum==digit
#     if digit==num:
#         print("it is peterson")
#     else:
#         print("it is not peterson")
# strong number
# import math
# num=int(input())
# digit_factorial=0
# for digit in str(num):
#     digit_factorial+=math.factorial(int(digit))
# if digit_factorial==num:
#     print("it is strong number")
# else:
#     print("it is not strong number")
