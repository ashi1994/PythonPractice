'''
Created on May 19, 2018

@author: aranjan
'''
text='Hello java'
print(text[0:3])#hel
print(text[3:])#io java
print(text.capitalize())#it will captialized the first character of string #Helio java
print(text.upper())#HELIO JAVA
print(text.lower())#helio java
print(len(text))
print(text.islower())#It returns True if the characters of a string are in lower case, otherwise False.
print(text.isupper())#It retuen True if the characters in Uppercase
print(text.count('a'))# It return count of a in string
print(text.find("H")) # find the word H in the string)
print(text.count(' '))
print(text.replace("Hello", "Goodbye"))
stesxt="   hello java"
print(stesxt)
print(stesxt.strip())#remove space
print(stesxt.rstrip())#remove right spaces