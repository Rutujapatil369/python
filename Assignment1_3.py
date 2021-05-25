# Write a program which contains one function named as Add() 
#which accepts two numbers  from user and return addition of that two numbers.  
#Input : 11 5 Output : 16 


def Add(No1,No2):
    return No1+No2
   
    
    
def main():
    print("Enter two numbers:")
    no1=int(input())
    no2=int(input())
    
    value=Add(no1,no2)
    print("Addition of {} and {} is {}:".format(no1,no2,value))
    
    

if __name__=="__main__":
    main()