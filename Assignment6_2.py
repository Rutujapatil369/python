"""
Write a program which contains one class named as Circle.  
Circle class contains three instance variables as Radius ,Area, Circumference.  
That class contains one class variable as PI which is initialise to 3.14.  
Inside init method initialise all instance variables to 0.0.  
The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,  CalculateCircumference(), Display().  
Accept method will accept value of Radius from user.  
CalculateArea() method will calculate area of circle and store it into instance variable Area.  
CalculateCircumference() method will calculate circumference of circle and store it into instance  variable Circumference.  
And Display() method will display value of all the instance variables as Radius , Area,  Circumference.  
After designing the above class call all instance methods by creating multiple objects.  
"""

class Circle:
    PI=3.14
    
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
        
    def Accept(self,i):
        self.Radius=i
       
      
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
    
    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
        
    def Display(self):
        print("Radius of circle is",self.Radius)
        print("Area of circle",self.Area)
        print("Circumference of circle is",self.Circumference)
        
def main():
    obj1=Circle()
    obj2=Circle()
    obj3=Circle()
    
    obj1.Accept(3)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    
    obj2.Accept(4)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()
    
    obj3.Accept(5)
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()
        
        
        

if __name__=="__main__":
    main()