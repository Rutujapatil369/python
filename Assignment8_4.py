"""
Design python application which creates three threads as small, capital, digits. 
All the  threads accepts string as parameter. 
Small thread display number of small characters,  capital thread display number of capital characters 
and digits thread display number of  digits. 
Display id and name of each thread.  
"""


import threading

def small(str):
    count=0
    for i in range(len(str)):
        if(str[i]>='a' and str[i]<='z'):
            count+=1
    print("Lower Count is:",count)
    
def capital(str):
    count=0
    for i in range(len(str)):
        if(str[i]>='A' and str[i]<='Z'):
            count+=1
    print("Upper Count is:",count)

def digit(str):
    count=0
    for i in range(len(str)):
        if(str[i]>='0' and str[i]<='9'):
            count+=1
    print("Digit Count is:",count)
    
    

def main():
    print("Enter string:")
    value=input()
    

    t1=threading.Thread(target=small,args=(value,))
    t2=threading.Thread(target=capital,args=(value,))
    t3=threading.Thread(target=digit,args=(value,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    main() 

