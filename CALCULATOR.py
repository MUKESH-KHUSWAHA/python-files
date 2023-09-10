#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mukes
#
# Created:     20/08/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
#------------------------------------------------------------------------------
def sum(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b != 0:
        return(a/b)
    else:
        return("NOT DEFINED")
try:


    choice=input('''select 1/2/3/4\n1.sum\n2.subtract\n3.multiply\n4.divide''' )
    a=int(input("enter any number"))
    b=int(input("enter second number"))
    if choice=="1":
        print(sum(a,b))
    elif choice=="2":
        print(subtract(a,b))

    elif choice=="3":
        print(multiply(a,b))

    elif choice=="4":
        print(divide(a,b))
    else:
        print("invalid input")

except:
    print("plz give input or give valid argument")