def Sum(No):
    value=0
    while(No>0):
        dig=No%10
        value=value+dig
        No=No//10
    return value

def main():
    print("Enter Number")
    value=int(input())
    ret=Sum(value)
    print("Addition is",ret)

if __name__=="__main__":
    main()