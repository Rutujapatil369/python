"""Create on module named as Arithmetic which contains 4 functions as 
Add() for addition, Sub()  for subtraction, Mult() for multiplication and Div() for division. 
All functions accepts two  parameters as number and perform the operation. 
Write on python program which call all the  functions from Arithmetic module by accepting the parameters from user.  
"""

from Arithematic import * 
def main():
    print("Enter first number")
    value1=int(input())
    
    print("Enter second number")
    value2=int(input())
    
    ret1=Add(value1,value2)
    ret2=Sub(value1,value2)
    ret3=Mult(value1,value2)
    ret4=Div(value1,value2)
    
    print("Addition is:",ret1)
    print("Subtraction is:",ret2)
    print("Multiplication is:",ret3)
    print("Division is:",ret4)
    
    
    

if __name__=="__main__":
    main()