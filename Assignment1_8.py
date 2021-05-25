#Write a program which accept number from user and print that number of “*” on screen.  

def PrintNum(No):
    for i in range(No):
        print("*")

def main():
    print("Enter number")
    value=int(input())
    PrintNum(value)

if __name__=="__main__":
    main() 