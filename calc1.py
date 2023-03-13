# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:43:55 2023

@author: XeL
"""

n1 = n2 = op = 0

print("----------Hello n welcome!----------\n\n")
print("this is py_calc v1, made with <3\n")
print("Pls type wich operation you want to make:\n")
print("1-Addition\n")
print("2-Substraction\n")
print("3-Decimal division\n")
print("4-Floor division\n")
print("5-Multiplication\n")
print("6-Exponentiation\n")
print("7-Modulus\n\n\n")

op = input("Enter option: ")
while not op.isdigit() or int(op) < 1 or int(op) > 8:
    op = input("Invalid Option. Enter option: ")
    
n1 = input("\n\nThx!, pls enter number 1: ")
while not n1.isdigit():
    n1 = input("Invalid Option. Pls enter number 1: ")

n2 = input("\n\nGreat!, pls enter number 2: ")
while not n2.isdigit():
    n2 = input("Invalid. Pls enter number 2: ")
