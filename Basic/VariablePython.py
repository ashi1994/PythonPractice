'''
Created on May 19, 2018

@author: aranjan
'''
'''
In Python when you want to use the same variable for rest of your program or module you declare
 it a global variable, 
while if you want to use the variable in a specific function or method, you use a local variable.
'''
class VarTest:
    a=101
    print(a)
    def locaLFunction(self):
        a="heloo java"
        print(a)
        
obj=VarTest()
obj.locaLFunction()