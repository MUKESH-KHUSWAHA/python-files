#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mukes
#
# Created:     21/08/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def factorial(n):
    if(n==0 or n==1):
        return (1)
    else:
        return (n * factorial(n-1))
n= int(input("enter any number "))
print(factorial(n))

 #fibonacci series
def fibonacci(f):
    if(f==0 or f==1):
        return(1)
    else:
        return(fibonacci(f-1)+fibonacci(f-2))
print(fibonacci(5))