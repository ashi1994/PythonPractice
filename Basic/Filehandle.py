'''
Created on May 19, 2018

@author: aranjan
'''
textfile=open("C:\\Users\\aranjan\\Desktop\\ashi.txt","r")
print("File name",textfile.name)
print("File mode",textfile.mode)
text=textfile.read(10)
print(text)
text1="hello ashiwani"
textfile.write(text1)#write to the file