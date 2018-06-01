'''
Created on May 17, 2018

@author: aranjan
'''
def myFunction(a,b):
    sum=a+b
    print(sum)
  
def myReturnFunction(a,b):
    return (a*b)    

def triangleType(x,y,z):
    if x==y and y==z and z==x: print("All are equal")
    elif x!=y and y!=z: print("Some problem")
    
    
myFunction(2,3)
sum=myReturnFunction(4, 10)
print(sum)
triangleType(10, 10, 10)
    