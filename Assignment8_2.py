"""
Design python application which creates two threads as evenfactor and oddfactor.  
Both the thread accept one parameter as integer. 
Evenfactor thread will display  addition of even factors of given number 
and oddfactor will display addition of odd  factors of given number. 
After execution of both the thread gets completed main  thread should display message as “exit from main”.  
"""

import threading
def EvenFactor(no):
    sum=0
    for i in range(1,no):
        if(no%i==0):
            print(i)
            if(i%2==0):
                sum+=i
    print("sum of even factors is:",sum)
    
def OddFactor(no):
    sum=0
    for i in range(1,no):
        if(no%i==0):
            print(i)
            if(i%2!=0):
                sum+=i
    print("sum  of odd factors is:",sum)

def main():
    print("Enter no:")
    no=int(input())
    t1=threading.Thread(target=EvenFactor,args=(no,))
    t2=threading.Thread(target=OddFactor,args=(no,))
    
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Exit from main")
    
if __name__=="__main__":
    main()