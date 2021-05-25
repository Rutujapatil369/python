"""
Design python application which creates two thread named as even and odd. 
Even  thread will display first 10 even numbers and odd thread will display first 10 odd  numbers.  
"""

import os 
import threading

def Even(no):
    no=no*2
    for i in range(1,no+1):
        
        if(i%2==0):
            print(i)
            
def Odd(no):
    no=no*2
    for i in range(1,no+1):
        
        if(i%2!=0):
            print(i)
    
            
    

def main():
    print("Enter no:")
    no=int(input())
    t1=threading.Thread(target=Even,args=(no,))
    t2=threading.Thread(target=Odd,args=(no,))
    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__=="__main__":
    main()