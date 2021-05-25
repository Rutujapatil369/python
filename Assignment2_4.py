#Write a program which accept one number form user and return addition of its factors.
#  Input : 12 Output : 16 (1+2+3+4+6)  

def FactAdd(No):
    sum=0
    i=0
    for i in range(1,No):
        if(No%i==0):
            sum=sum+i
            
    return sum
            
def main():
    print("Enter Number")
    value=int(input())
    ret=FactAdd(value)
    print("Sum of factorial is",ret)
    

if __name__=="__main__":
    main()