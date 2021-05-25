""" Write a recursive program which accept number from user and return its  factorial.  
Input : 5  
Output : 120  
"""

def FactNo(no):
    i=0
    if(no==0):
        return 1
    else:
        return no*FactNo(no-1)

def main():
    print("Enter the number")
    value=int(input())
    ret=FactNo(value)
    print("Factorial of number is",ret)

if __name__=="__main__":
    main()