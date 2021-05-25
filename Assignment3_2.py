"""Write a program which accept N numbers from user and store it into List. 
Return Maximum  number from that List.  
Input : Number of elements : 7  
Input Elements : 13 5 45 7 4 56 34  
Output : 56  
"""

def Max(List):
    return max(List)
      

def main():
    arr=[]
    print("Enter numbers u want in list")
    size=int(input())
    for i in range(size):
        print("Enter number",i+1)
        number=int(input())
        arr.append(number)
    print("Accepted data is",arr)
    
    ret=Max(arr)
    print("Max number in list is",ret)

if __name__=="__main__":
    main()