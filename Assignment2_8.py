#Write a program which accept one number and display below pattern.  
#Input : 5  
  
#Output : 1  
 #1 2  
 #1 2 3  
 #1 2 3 4  
 #1 2 3 4 5  


def pattern(No):
    
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end="")
            
        print("")
      
    
def main():
    print("Enter Number")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()