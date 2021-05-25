"""
Design python application which contains two threads named as thread1 and thread2. 
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on  screen.
After execution of thread1 gets completed then schedule thread2. 
"""

import threading

def Thread1():
    for i in range(1,51):
        print("Normal order:",i)
        
def Thread2():
    for i in range(50,0,-1):
        print("Reverse order:",i)

def main():

    t1=threading.Thread(target=Thread1,args=())
    t2=threading.Thread(target=Thread2,args=())
    
    t1.start()
    t1.join()
    t2.start()
    t2.join()

if __name__=="__main__":
    main()