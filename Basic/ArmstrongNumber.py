'''
Created on May 19, 2018

@author: aranjan
'''
num=int(input("Enter a number"))
temp=num
sum=0
while(temp>0):
    num=temp//10
    rem=temp%10
    sum=sum+rem**3
    
if sum==num:
    print("Armstrong number")
else:
    print("Not armstrong number")


