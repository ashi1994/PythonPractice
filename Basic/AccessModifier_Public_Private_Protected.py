'''
Created on May 31, 2018

@author: aranjan
'''
class parent1:
    name='ashiwani'#This is public
    __age=21 #This is private
    _sex='male' # This is protected
class child(parent1):
    def show(self):
        print(self.name)
        #print(self.__age)
        print(self._sex)
obj=child()
obj.show()