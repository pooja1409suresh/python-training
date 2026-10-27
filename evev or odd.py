# even or odd using bitwise
#def check_even_odd(number):
 #    if number&1:
 #       return"odd"
    # else:
 #       return"even"
#print(check_even_odd(8))

# conditional statement
#cgpa=float(input())
#dep=input()
#if cgpa>=8 and dep=="IT":
#   print("your are eligible")
#else:
#   print("your are not eligible")

# using ternary operator
# age=int(input("Enter your age: "))
# i="eligible" if age>=18 else"not"
# print(i)

# 5 table
#for i in range (1,10):
#   a=i*5
#   print("5x",i,"=",a)

# n=int(input())
# for i in range (1,11):
#    a=i*n
#    print(n ,"x",i,"=",a)

#find the prime number with user given range
# n=int(input("enter: "))
# m=int(input("enter: "))
# count=0
# for i in range(n,m+1):
#    if i>1:
#       for j in range(2,i):
#         if i%j==0:
#            break
#       else: 
#          count+=1
#          print(i) 
# print(count)
   
# a=input()
# count=0
# char_list=[]
# for i in a:  
#  count+=1
#  char_list+=i
# print(char_list)
# print("count: ",count)

# consnant
# a=input()
# v='aeiouAEIOU'
# count=0
# for i in a:
#     if i not in v:
#         count+=1
#         print("consonant")
# print("count: ",count)

# vowels
# a=input()
# v='aeiouAEIOU'
# count=0
# for i in a:
#     if i in v:
#         count+=1
# print("count: ",count)

# password
# password = input("Enter your password: ")
# has_alphabet = False
# has_number = False
# has_special = False
# for char in password:
#     ascii_val = ord(char)
#     if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
#         has_alphabet = True
#     elif 48 <= ascii_val <= 57:
#         has_number = True
#     elif char != " ":  
#         has_special = True
# if has_alphabet and has_number and has_special:
#     print("Strong password!")
# else:
   #  print("Weak password. Missing requirements:")
   #  if not has_alphabet:
   #      print("- Must include at least one letter")
   #  if not has_number:
   #      print("- Must include at least one number")
   #  if not has_special:
   #      print("- Must include at least one special character")

#palindrom
# s=input()
# if s==s[::-1]:
#     print("equal")
# else:
#     print("not")

# s="hello"
# print("w"+s[1:])

#using f-string
# name=input("enter a name: ")
# age=input("enter your age: ")
# print(f"my name is {name} and my age is {age}")

# reversing the string and checking the equality
# n=input()
# if n[0]==n[-1]:
#     print("yes")
# else:
#     print("not")

# v=input()
# a=input()
# count=0
# for i in v:
#     if a is i:
#         count+=1
# print(count)

# text=input("enter a string")
# seen=[]
# duplicates=[]
# for char in text:
#    if char==" ":
#        continue
#    if char in seen:
#        if char not in duplicates:
#            duplicates.append(char)
#    else:
#        seen.append(char)
# print("duplicates: ",duplicates)


# t= input()
# count=0
# for char in t:
#     if t.count(char) == 1:
#         print(f"The first non-repeating character is: '{char}'")
#         break
# else:
#    print("All characters repeat or the string is empty")

# duplicate char in str
# s = "programming"
# for i in range(len(s)):
#     if s[i] in s[i+1:]:
#         print(s[i])

# non repeating char in str
# s="pooja" 
# count=0
# for i in range(len(s)):
#     if s[i]not in s[:i]and s[i]not in s[i+1:]:
   
#         print(s[i])
#         print(s.count(s[i]))
#         break    

# s=input()
# for char in s:
#     print(s[-3:])
#     break

# s="hello"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.replace(" ","").upper())
# print("".join(s.split()))
# print(s.split())
# l=[]
# for i in s:
#     l+=i
# print(l)

# s=input()
# l=s.split()
# count=0
# for i in l:
    
#     count+=1
# print("count: ",count)

# count vowels and consonant,igore digit,space and punctuation sample input:hello 123 op:vowels.consonants
# text=input()
# vowels="aeiou"
# consnant="bcdfghjklmnpqrstvwxyz"
# v=0
# c=0
# for i in text:
#    if i in vowels:
#        v+=1
#    if i in consnant:
#       c+=1
# print(v,c)
    
# COUNT:WORDS STARTING WITH VOWELS 
#1
# a=input()
# vowel=("a","e","i","o","u")
# count=0
# for i in a.lower().split():
#     if i.startswith(vowel):
#         count+=1
# print(count)

#2
#    if i and i[0] in vowel:
#       count+=1
# print(count)

# replace * with vowels
n=input()
vowel="aeiouAEIOU"
s=""
for i in n:
    if i in vowel:
        s+="*"
    else:
        s+=i
print(s)