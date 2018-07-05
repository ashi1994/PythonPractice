'''
Created on May 18, 2018

@author: aranjan
'''
#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.


thisdict =    {
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
#Iterate the Dictionqry
for key in thisdict:
    print (key, thisdict[key])
#Iterating over (key, value) pairs
for (key, value) in thisdict.items():
    print (key, value)    
# Change apple colur to red
thisdict["apple"] = "red"
print(thisdict)


thatdict = dict(apple="green", banana="yellow", cherry="red")
thatdict["damson"] = "purple"
print(thatdict)
print(len(thatdict))
print(thisdict.keys())
print(thisdict.values())