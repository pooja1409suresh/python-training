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
   
#count the string
#  a=input()
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
'''n=input()
if n[0]==n[-1]:
    print("yes")
else:
    print("not")
'''
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

# s="hello world"
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
# n=input()
# vowel="aeiouAEIOU"
# s=""
# for i in n:
#     if i in vowel:
#         s+="*"
#     else:
#         s+=i
# print(s)

#join and split use
#1
# n=input()
# a=" ".join(i [::-1] for i in n.split())
# print(a)
#2
# n=input()
# l=n.split()
# for i in l:
#    print (i[::-1],end=" ")

#anagram
# a=input()
# b=input()
# is_anagram=len(a)==len(b)
# for char in a:
#     if a.count(char)!=b.count(char):
#         is_anagram=False
# print("anagram"if is_anagram else"not anagram")

#leetcode:771
'''def numJewelsInStones(jewels:str,stones:str)->int:
    count =0
    for stone in stones:
        if stone in jewels:
            count +=1
            return count
print(numJewelsInStones("aA","aAAbbbb"))'''

# anagram sort tech
# a=input()
# b=input()
# if sorted(a)==sorted(b):
#     print("anagram")
# else:
#     print("not anagram")

# n=input()
# for i in n:
#     if n.replace ("n.islower","n.isupper"):
#          print(i)

# n=input()
# r=n.swapcase()
# print(r)

# n=input()
# u=""
# for i in n:
#     if i.islower():
#         u+=i.upper()
#     elif i.isupper():
#         u+=i.lower()
#     elif i.isdigit():
#         u+=i
# print(u)

# n=input()
# d={}
# for i in n:
#   if i in d:
#      d[i]+=1
#   else:
#      d[i]=1
# print(d)
# print((max(d,key=d.get)), ":", max(d.values()))

# n=int(input())
# if 1<=n<=100:
#     if n%2!=0:
#         print("Weird")
#     elif n%2==0 and n in range(2,6):
#         print("Not Weird")
#     elif n%2==0 and n in range(6,21):
#         print("Weird")
#     elif n%2==0 and n>20:
#         print("Not Weird")
#     else:
#         print("empty")
   
# year=int(input())
# if year%4==0 and year%100!=0 or year%400==0:
#     print("true")
# else:
#         print("false")

# palindromic method 1
# s=["abc","car","ada","racacar","cool"]
# found=False
# for i in s:
#     if i==i[::-1]:
#         print(f"the first palindromic string:,{i}")
#         found=True
#         break
# if not found:
#     print("not palindromic")

# palindromic method 2
# s=["abc","car","ada","racacar","cool"]
# for i in s:
#     if i==i[::-1]:
#         r=i
#         break
#     else:
#         r=""
# print(r)

'''def poojha(nums):
   r,s=[],[]
   for i in nums:
      if i!=0:
         r+=str(i)
      if i==0:
         s+=str(i)  
   return r,s
print(poojha([1,2,30,0,10,0]))     ''' 

'''list=[]
n=int(input())
t=0
for i in range(n):
    list.append(i)
print(list)
for i in list:
    t+=i
print(t,t//len(list))'''

# n=int(input())
# list=[]
# r,s=[],[]
# for i in range(n):
#     i=int(input())
#     list.append(i)
# print(list)
# for i in list:
#     if i!=0:
#         r.append(i)
#     else:
#         s.append(i)
# print(r+s)
    
'''n=[1,21,52,8]
min=n[0]
max=n[0]
for i in n:
    if i>max:
       max=i
    if i<min:
        min=i
print(max)
print(min)'''

'''n=[1,21,52,8]
print(max(n),min(n))
'''

'''n=int(input())
arr=[]
for i in range(n):
    i=int(input())
    arr.append(i)
max_2=max(arr)
for i in arr:
    if i==max_2:
        arr.remove(i)
max=0
for i in arr:
    if i>max:
        max=i
print(max)'''

'''t=("e","r",[1,2],"g")
print(t[2][1])
t[2]=3
print(t)
r=("k")
print(type(r))'''

'''n=int(input())
t=tuple(int(x) for x in input().split(","))
count=0
for i in t:
   if i==n:
        count+=1
   else:
         pass
print(n,count)'''

'''n=int(input("range:"))
target=int(input("target:"))
t,count=(),0
for i in range(n):
    i=int(input())
    t=t+(i,)
print(t)
for i in t:
   if i==target:
        count+=1
   else:
       pass
print("tuple:",t,"count:",count)
'''
#leetcode:1480, running sum 
#1
'''n=list(map(int,input("enter number:").split()))
c=[]
t=0
for i in n:
    t+=i
    c.append(t)
print(c)
'''
#2
'''class Solution(object):
   def moveZeroes(self, nums):
      c=[]
      t=[]
      for i in nums:
       i.remove[0]
       c==i
      return c
      for c in 
        c.append[0]     
        t==c
      return t
print(t)'''

# moving zeros to last,leetcode: 283
'''f=list(map(int,input("enter number:").split()))
t=[]
c=[]
for i in f:
    if i==0:
        c.append(i)
    if i !=0:
        t.append(i)
print(t+c)'''

# leetcode:1768 
'''word1=input()
word2=input()
result=""
for i in range(min(len(word1),len(word2))):
    result+=word1[i]
    result+=word2[i]
result+=word2[min(len(word2),len(word1)):]
result+=word1[min(len(word2),len(word1)):]

print(result)'''

# leetcode:2108
'''class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n=""
        for i in words:
            if i==i[::-1]:
                n=i 
                break  
            else:
                n= ""
        return n  '''  

# a={1,2,3}
# b={2,5,7}
# print(a|b)

# n=input()
# m=n.split()
# print (set(m))
