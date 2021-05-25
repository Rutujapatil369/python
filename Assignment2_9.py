#Write a program which accept number from user and return number of digits in that number. 

def Count(No):
    count=0
    while(No>0):
        count=count+1
        No=No//10
    return count
    
    
def main():
    print("Enter Number")
    value=int(input())
    ret=Count(value)
    print("Length is",ret)

if __name__=="__main__":
    main()