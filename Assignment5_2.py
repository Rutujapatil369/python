"""Write a recursive program which display below pattern.  
Input : 5  
Output : 1 2 3 4 5  
"""

def pattern(no):
    if(no>0):
        no=no-1
        pattern(no)
        print(no+1)     
          

def main():
    print("Enter the number")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()