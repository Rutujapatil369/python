# Write a program which accept one number and display below pattern.  
#Input : 5  
"""Output : 
 * * * * *  
 * * * * * 
 * * * * *  
 * * * * *  
 * * * * * 
""" 



def Pattern(No):
    for i in range(No):
        for j in range(No):
            print("*",end="")
        print("")
    

def main():
    print("Enter Number")
    value=int(input())
    Pattern(value)

if __name__=="__main__":
    main()