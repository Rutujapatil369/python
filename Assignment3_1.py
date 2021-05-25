"""Write a program which accept N numbers from user and store it into List. 
Return addition of all  elements from that List.  
Input : Number of elements : 6  
Input Elements : 13 5 45 7 4 56  
Output : 130 
""" 


def AdditionInList(List):
    sum=0
    for i in range(len(List)):
        sum=sum + List[i]
    return sum

def main():
    
    arr=[]
    print("Enter numbers u want in list")
    size=int(input())
    for i in range(size):
        print("Enter number",i+1)
        number=int(input())
        arr.append(number)
    print("Accepted data is",arr)
    
    ret=AdditionInList(arr)
    print("Addition of numbers in list is",ret)
    

if __name__=="__main__":
    main()