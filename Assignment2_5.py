#.Write a program which accept one number for user and check whether number is prime or not. 
def CheckPrime(No):
    if(No==1):
        print("Not Prime number")
    if(No>1):
        for i in range(2,No):
            if(No%i==0):
                print("NOt prime")
                break
        else:
            print("prime number")
    else:
        ("No is not prime")


def main():
    print("Enter Number")
    value=int(input())
    CheckPrime(value)

if __name__=="__main__":
    main()