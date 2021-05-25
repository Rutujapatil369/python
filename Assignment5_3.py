"""Write a recursive program which display below pattern.  
Input : 5  
Output : 5 4 3 2 1 
"""

def pattern(no):  
    if(no>0): 
        no=no-1
        print(no+1)
        pattern(no)
        
           
          

def main():
    print("Enter the number")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()