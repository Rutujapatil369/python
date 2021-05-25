"""Write a program which accept N numbers from user and store it into List. 
Accept one another  number from user and return frequency of that number from List.  
Input : Number of elements : 11  
Input Elements : 13 5 45 7 4 56 5 34 2 5 65  Element to search : 5  
Output : 3  
"""

def Search(List,key):
    count=0
    for i in range(len(List)):
        if(List[i]==key):
            count+=1
    return count

def main():
    arr=[]
    print("Enter numbers u want in list")
    size=int(input())
    for i in range(size):
        print("Enter number",i+1)
        number=int(input())
        arr.append(number)
    print("Accepted data is",arr)
    
    print("Enter element to search")
    key=int(input())
    
    ret=Search(arr,key)
    print("{} found {} times in list".format(key,ret))

if __name__=="__main__":
    main()