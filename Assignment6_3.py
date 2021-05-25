"""Write a program which contains one class named as Arithmetic.  
Arithmetic class contains three instance variables as Value1 ,Value2.  
Inside init method initialise all instance variables to 0.  
There are three instance methods inside class as Accept(), Addition(), Subtraction(),  Multiplication(), Division().  
Accept method will accept value of Value1 and Value2 from user.  
Addition() method will perform addition of Value1 ,Value2 and return result.  
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.  
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.  
Division() method will perform division of Value1 ,Value2 and return result.  
After designing the above class call all instance methods by creating multiple objects.  
  
"""

class Arithematic:
    
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self,i,j):
        self.value1=i
        self.value2=j
        
    def Addition(self):
        return self.value1+self.value2
        
    def Substraction(self):
        return self.value1-self.value2
    
    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2
        
def main():
    obj1=Arithematic()
    obj2=Arithematic()
    obj3=Arithematic()
    
    obj1.Accept(12,4)
    ret=obj1.Addition()
    print("Addition from obj1 is:",ret)
    ret=obj1.Substraction()
    print("Substraction from obj1 is:",ret)
    ret=obj1.Multiplication()
    print("Multiplication from obj1 is:",ret)
    ret=obj1.Division()
    print("Division from obj1 is:",ret)
    
    obj2.Accept(100,20)
    ret=obj2.Addition()
    print("Addition from obj2 is:",ret)
    ret=obj2.Substraction()
    print("Substraction from obj2 is:",ret)
    ret=obj2.Multiplication()
    print("Multiplication from obj2 is:",ret)
    ret=obj2.Division()
    print("Division from obj2 is:",ret)
    
    obj3.Accept(20,4)
    ret=obj3.Addition()
    print("Addition from obj3 is:",ret)
    ret=obj3.Substraction()
    print("Substraction from obj3 is:",ret)
    ret=obj3.Multiplication()
    print("Multiplication from obj3 is:",ret)
    ret=obj3.Division()
    print("Division from obj3 is:",ret)
    
if __name__=="__main__":
    main()  
    
    
    
    