"""Write a program which accept N numbers from user and store it into List. Return Minimum  number from that List.  
Input : Number of elements : 4  
Input Elements : 13 5 45 7  
Output : 5 
""" 


def Min(List):
    List.sort()
    return List[0]

def main():
    arr=[]
    print("Enter numbers u want in list")
    size=int(input())
    for i in range(size):
        print("Enter number",i+1)
        number=int(input())
        arr.append(number)
    print("Accepted data is",arr)
    
    ret=Min(arr)
    print("Minimun number in list is",ret)

if __name__=="__main__":
    main()