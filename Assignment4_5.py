"""Write a program which contains filter(), map() and reduce() in it. 
Python application which  contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter  should filter out all prime numbers. 
Map function will multiply each number by 2. Reduce will  return Maximum number from that numbers.  
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]  
List after filter = [2, 11, 17, 23, 31]  
List after map = [4, 22, 34, 46, 62]  
Output of reduce = 62  
"""

import functools
def ChkPrime(No):
    if(No==1):
        return False
    if(No>1):
        for i in range(2,No):
            if(No%i==0):
                return False
                break
        else:
            return True
    else:
        return False

    
def fun1(no):
    return no*2
    
def fun2(no1,no2):
    if(no1>no2):
        return no1
    else:
        return no2


def main():
    arr=[]
    print("Enter number of elements")
    size=int(input())
    
    for i in range(size):
        print("Enter element number:",i+1)
        no=int(input())
        arr.append(no)
    print("Your entered data is",arr)
    
   
    newdata=list(filter(ChkPrime,arr))   
    print("After filtering data is",newdata)
    
    newdata1=list(map(fun1,newdata))   
    print("After map data is",newdata1)
    
    newdata2=functools.reduce(fun2,newdata1)  
    print("After reduce data is",newdata2)
    
    
if __name__=="__main__":
    main()