'''
Created on May 20, 2018

@author: aranjan
'''
def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
fact1=int(input("input a number for which you want factorial"))
if(fact1<0):
    print('factorail does not exist')
else:
    print(fact(fact1))