'''
Created on May 18, 2018

@author: aranjan
'''
original='Hello java'
# Function to reverse a string Using extended slice syntax
def reverse(string):
    string = string[::-1]
    return string

#Function to reverse a string
def reverse1(string):
    string = "".join(reversed(string))
    return string
 
#rev=reverse(original)
print(reverse(original))
rev=reverse1(original)
print(rev)