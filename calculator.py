class calculator:

    def __init__(self ,a ,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"the addition of {self.a}and { self.b} is {self.a+self.b}")
    
    def substract(self):
        print(f"the substraction  of {self.a}and { self.b} is {self.a-self.b}")

    def multiply(self):
        print(f"the multiplication  of {self.a}and { self.b} is {self.a*self.b}")

    def divide(self):
        print(f"the division of {self.a}and { self.b} is {self.a/self.b}")

a=calculator(89,389)  
a.add() 
a.substract()  
a.multiply()
a.divide()
