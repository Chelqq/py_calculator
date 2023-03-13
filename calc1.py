# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:43:55 2023

@author: XeL
"""
from os import system, name
from time import sleep
n1 = n2 = op = 0

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        system("clear")

print("----------Hello n welcome!----------\n\n")
print("this is py_calc v1, made with <3\n")
print("Pls type wich operation you want to make:\n")
print("1-Addition\n")
print("2-Substraction\n")
print("3-Decimal division\n")
print("4-Floor division\n")
print("5-Multiplication\n")
print("6-Exponentiation\n")
print("7-Modulo\n\n\n")

op = input("Enter option: ")
while not op.isdigit() or int(op) < 1 or int(op) > 8:
    op = input("Invalid Option. Enter option: ")
op = int(op)
    
n1 = input("\n\nThx!, pls enter number 1: ")
while not n1.isdigit():
    n1 = input("Invalid Option. Pls enter number 1: ")
n1 = int(n1)

n2 = input("\n\nGreat!, pls enter number 2: ")
while not n2.isdigit():
    n2 = input("Invalid. Pls enter number 2: ")
n2=int(n2)


clear()
sleep(1)
print("\n\nthinking...\n")
sleep(2)
print("beep bop\n")
sleep(2)
print("ran out of fingers, but the anwser is: ")

if op == 1:     #add
    print(n1+n2)
if op == 2:
    print(n1-n2)
if op == 3:
    print(n1/n2)
if op == 4:
    print(n1 // n2)
if op == 5: 
    print(n1*n2)
if op == 6:
    print(n1 ** n2)
if op == 7:
    print(n1 % n2)
    
    

