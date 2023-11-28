class Calulator:
    def add (self, a, b):
        return a + b
    
    def substract(self , a, b ):
        return a-b
    
    def multiply(self , a, b ):
        return a*b
    
    def division(self , a, b ):
        try:
            return a/b
        except:
            return "Division by zero error"
            
while True:  
    cal = Calulator()
    a= float(input("enter a :- "))
    b= float(input("enter b :- "))
    op= input("enter operator :- ")

    if op == "*" :
        result = cal.multiply(a,b)
    elif op == "+" :
        result = cal.add(a,b)
    elif op == "-" :
        result = cal.substract(a,b)
    elif op == "/" :
        result = cal.division(a,b)
    
    print("Result is :",result)
