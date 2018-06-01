'''
Created on May 18, 2018

@author: aranjan
'''
class Parent:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello' + name)
        else:
            print('Hello') 
     
        obj=Parent()
        obj.sayHello()
        obj.sayHello('Ashiwani')
 