'''
Problem Statement:
Write a program to print a dictionary where the keys are numbers
between 1 and 15 and the values are cube of keys.
''' 
print('Program to print a dictionary where the keys are numbers, and the values are cube of respective keys. ')

#make a new empty dictionary
cubes=dict()

#using for loop
for i in range(1,16):
    cubes[i]= i*i*i
    
#output
print("\n\t'KEY' : 'VALUE' ")
for key,value in cubes.items():
    print('\t',key, ' : ',value)
   
print()