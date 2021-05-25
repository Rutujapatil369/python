def Fact(No):
    if(No==1):
        return No
    else:
        return No*Fact(No-1)

def main():
    print("Enter Number")
    value=int(input())
    ret=Fact(value)
    print("Factorial of {} is {}".format(value,ret))

if __name__=="__main__":
    main()