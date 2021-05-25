"""
Design python application which creates two threads as evenlist and oddlist. 
Both the  threads accept list of integers as parameter. 
Evenlist thread add all even elements  from input list and display the addition. 
Oddlist thread add all odd elements from input  list and display the addition. 
"""

import threading

def EvenList(value):
    sum=0
    for i in value:
        if(i%2==0):
            sum+=i
    print("Sum of even from list:",sum)

def OddList(value):
    sum=0
    for i in value:
        if(i%2!=0):
            sum+=i
    print("Sum of odd from list:",sum)
            

def main():
    value=[]
    print("Enter the number of elements in list:")
    size=int(input())
    for i in range(size):
        print("Enter the number")
        no=int(input())
        value.append(no)
    print("Accepted data is",value)

    t1=threading.Thread(target=EvenList,args=(value,))
    t2=threading.Thread(target=OddList,args=(value,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__=="__main__":
    main()