'''
Created on May 17, 2018

@author: aranjan
'''
n=int(input('Enter a number '))
rev=0
temp=n
while(n>0):
    a=n%10
    n=n//10# Normal / will give decimal value after the integer
    rev=rev*10+a
        
print("Reverse is  ",rev)   

if(temp==rev):
    print("Palindrome")
else:
    print("Not palindrome")