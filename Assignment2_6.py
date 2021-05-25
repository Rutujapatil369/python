# Write a program which accept one number and display below pattern.  
#Input : 5  
#Output :
""" 
 * * * * *  
 * * * *  
 * * *  
 * *  
 *
""" 

def pattern(No):
    #for i in range(0,No):
       # No=No-1
       # print("*"*(No+1))
        
    for i in range(No+1,0,-1):
        for j in range(0,i-1):
            print("*",end="")
        print("")
            
        

def main():
    print("Enter Number")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()