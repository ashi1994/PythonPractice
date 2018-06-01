'''
Created on May 17, 2018

@author: aranjan
'''
term=int(input("Please enter number of term"))
def fibo(num):
    if(num<=0):return num
    else:return fibo(num-1)+fibo(num-2)

for i in range(term):
    print(fibo(i))
    
#Another way to fibonacci
a=0
b=1
for j in range(1,10):
    print(a)
    c=a+b
    a=b
    b=c
    