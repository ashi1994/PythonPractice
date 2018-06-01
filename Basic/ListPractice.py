'''
Created on May 18, 2018

@author: aranjan
'''
#A list is a collection which is ordered and changeable. 
#In Python lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1]='mango'
print(thislist)

thislist.append("grape")
print(thislist)
print(len(thislist))

thislist.remove("cherry")
print(thislist)

print(len(thislist))

#Constructer list
newList=list(("hello","hi","bye"))
newList.reverse()
print('Reverse List',newList)
print("Size of list",len(newList))

#Remove last value
newList.pop()
print(newList)
# Iterating list
for fruits in thislist: print("Fruits are",fruits)