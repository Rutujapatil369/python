#Write a program which contains one function that accept one number from user.
#returns  true if number is divisible by 5 otherwise return false.

def CheckDivisible(No):
    if(No%5==0):
        return True
    else:
        return False

def main():
    print("Enter number")
    value=int(input())
    ret=CheckDivisible(value)
    
    if(ret==True):
        print("True")
    else:
        print("False")
    
    

if __name__=="__main__":
    main()