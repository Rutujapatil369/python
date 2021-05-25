"""Write a program which accept N numbers from user and store it into List. 
Return addition of all  prime numbers from that List. Main python file accepts N numbers from user and pass each  number to ChkPrime() function which is part of our user defined module named as  MarvellousNum. Name of the function from main python file should be ListPrime().  
Input : Number of elements : 11  
Input Elements : 13 5 45 7 4 56 10 34 2 5 8  Output : 54 (13 + 5 + 7 +2 + 5) 
""" 


from MarvellousNum import * 

def ListPrime(List):
    sum=0
    for i in List:
        sum=sum+i
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
    
    
    ret=ChkPrime(arr)
    print("accepted prime num list is",ret)
    
    ret1=ListPrime(ret)
    
    print("Addition of prime numbers in list is",ret1)
        
    

if __name__=="__main__":
    main()