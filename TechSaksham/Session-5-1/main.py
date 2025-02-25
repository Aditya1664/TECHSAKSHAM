# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:13:37 2025

@author: doshi
"""
# import my_module
# from math_pkg.operations import *
# #my_module.even()

# ch=int(input("Enter your choice: 1.Greet, 2.Add, 3.Subtract, 4.Multiply, 5.Divide :"))

# if ch==1:
#     my_module.greet("Dexter")

# elif ch==2:
#     print(add(4,5))
# elif ch==3:
#     print(sub(4,5))
# elif ch==4:
#     print(mul(4,5))
# elif ch==5:
#     print(divide(4,5))
# else:
#     print("Incorrect Choice.")

with open("untitled4.txt",'r') as file:
    content=file.read()
    print(content)
    
with open("untitled4.txt",'w') as file:
    file.write("Java is my favourite subject.")
    print(content)
    
with open("untitled4.txt",'r') as file:
    content=file.read()
    print(content)
    
with open("untitled4.txt",'a') as file:
    file.write("We are in a training now.")
    
with open("untitled4.txt",'r') as file:
    content=file.read()
    print(content)
    print(file.closed)
    
