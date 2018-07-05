'''
Created on May 18, 2018

@author: aranjan
'''
try:
    a=10/0
except ZeroDivisionError:
    print("error occured") 
#except IOError:
#except EOFError:
#except NameError:
#except TypeError:
else:
    print("Same")
finally:
    print("alwsays run")                