""".Write a program which contains filter(), map() and reduce() in it. 
Python application which  contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter  should filter out all such numbers which are even. 
Map function will calculate its square.  Reduce will return addition of all that numbers.  
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]  
List after filter = [2, 4, 4, 2, 8, 10]  
List after map = [4, 16, 16, 4, 64, 100]  
Output of reduce = 204  
"""

import functools

def CheckEven(no):
    #return(no%2)
    if no%2==0:
        return True
    else:
        return False

def fun1(no):
    return no*no
    
def fun2(no1,no2):
    return no1+no2
    
                

def main():
    arr=[]
    print("Enter number of elements")
    size=int(input())
    
    for i in range(size):
        print("Enter element number:",i+1)
        no=int(input())
        arr.append(no)
    print("Your entered data is",arr)
    
   
    newdata=list(filter(CheckEven,arr))   
    print("After filtering data is",newdata)
    
    newdata1=list(map(fun1,newdata))   
    print("After map data is",newdata1)
    
    newdata2=functools.reduce(fun2,newdata1)  
    print("After reduce data is",newdata2)
    
    
if __name__=="__main__":
    main()