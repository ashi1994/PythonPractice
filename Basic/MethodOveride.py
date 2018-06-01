'''
Created on May 18, 2018

@author: aranjan
'''
class Parent:
    def show(self):
        print("Parent Hello")
    def display(self):
        print("Parent Hi")
class Child(Parent):
    def show(self):
        print("Child hello")
    def display(self):
        print("Chile Hi")
obj=Child()
obj1=Parent()
obj.show()
obj.display()
obj1.show()
obj1.display()
                