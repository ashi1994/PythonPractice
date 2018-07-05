'''
Created on May 20, 2018

@author: aranjan
'''
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[7,8,9],[4,5,6],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]
# iterate through rows  
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):  
        result[i][j] = matrix1[i][j] + matrix2[i][j]  
for r in result:
    print(r)
#Multiplication
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j] 
for r in result:
    print(r) 
#Transpose of matrix 1 
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[j][i] = matrix1[i][j]  
for r in result:
    print(r)  