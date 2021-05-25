# Write a program which accept name from user and display length of its name.  
def CountLength(value):
    sum=0
    for i in value:
        sum+=1
    return sum
        
        

def main():
    print("Enter name")
    name=input()
    ret=CountLength(name)
    print("Length is",ret)

if __name__=="__main__":
    main() 