""" Write a recursive program which display below pattern.  
Input : 5  
Output : * * * * * 
"""

def pattern(no):
    i=1
    if(i<no):
        no=no-1
        pattern(no)
    print("*")
   


def main():
    print("Enter the number")
    value=int(input())
    pattern(value)

if __name__=="__main__":
    main()