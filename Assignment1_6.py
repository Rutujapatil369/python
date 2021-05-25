#.Write a program which accept number from user.
#check whether that number is positive or  negative or zero. 

def CheckNum(No):
    if(No>0):
        print("Positive Number")
    elif(No==0):
        print("Zero")
    else:
        print("Negative Number")
        
def main():
    print("Enter number")
    value=int(input())
    CheckNum(value)
    
    
if __name__=="__main__":
    main()