'''
Created on May 18, 2018

@author: aranjan
'''
class A:
    def show(self):
        print('hello')
class B:
    def display(self):
        print('java')
class Cl(A, B):
    obj2=Cl()
    obj2.show()
    obj2.display()       