""".Write a program which contains one lambda function which accepts two parameters 
and return  its multiplication.  
Input : 4 3 Output : 12  
Input : 6 3 Output : 18  
"""

Mult=lambda no1,no2:no1*no2

def main():
    print("Enter firt number")
    value1=int(input())
    
    print("Enter second number")
    value2=int(input())
    
    ret=Mult(value1,value2)
    
    print("Multiplication is",ret)
    
if __name__=="__main__":
    main()