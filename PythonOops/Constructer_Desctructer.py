'''
Created on May 19, 2018

@author: aranjan
'''
class Cons:
    def __init__(self,name,age):#parametrized constructer
        self.name=name
        self.age=age
        def __init__(self):#Non parametrized constructers
            print("i am non parametrized constructers")
        def show():
            print("Name is",self.name)
        def __del__(self): # Destructer
            print("I can destruct anything")
        cons=Cons()    
        cons1=Cons('ashiwani','28')
        cons2=Cons('ram','32')
        cons1=cons2
        del cons2
        print("deletee cons2")
        print(cons1)
        cons.show()