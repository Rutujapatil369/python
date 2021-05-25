""".Write a program which contains filter(), map() and reduce() in it. 
Python application which  contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter  should filter out all such numbers which greater than or equal to 70 and less than or equal to  90. 
Map function will increase each number by 10. Reduce will return product of all that  numbers.  
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]  
List after filter = [76, 89, 86, 90, 70]  
List after map = [86, 99, 96, 100, 80]  
Output of reduce = 6538752000  
"""

import functools
def fun1(no):
    if(no>=70 and no<=90):
        return True
    else:
        return False

def fun2(no):
    return no+10
    
def fun3(no1,no2):
    return no1*no2
    
                

def main():
    arr=[]
    print("Enter number of elements")
    size=int(input())
    
    for i in range(size):
        print("Enter element number:",i+1)
        no=int(input())
        arr.append(no)
    print("Your entered data is",arr)
    
   
    newdata=list(filter(fun1,arr))   
    print("After filtering data is",newdata)
    
    newdata1=list(map(fun2,newdata))   
    print("After map data is",newdata1)
    
    newdata2=functools.reduce(fun3,newdata1)  
    print("After reduce data is",newdata2)
    
    
if __name__=="__main__":
    main()