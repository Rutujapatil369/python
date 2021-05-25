"""Write a recursive program which accept number from user and return  summation of its digits.  
Input : 879  
Output : 24 
"""

sum=0
def AddDigit(no):
    global sum
    if(no>0):
        rem=no%10
        sum=sum+rem
        no=no//10
        AddDigit(no)   
    return sum
    
def main():
    print("Enter the number")
    value=int(input())
    ret=AddDigit(value)
    print("Sum is",ret)

if __name__=="__main__":
    main()