from abc import ABC,abstractmethod

class Calculator(ABC):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    @abstractmethod
    def calculate(self):
        pass
    
class Sum(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def calculate(self):
        return self.a+self.b
    
class Multiply(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def calculate(self):
        return self.a*self.b
    
# são aceitos ints e floats

print(Sum(2,3.0).calculate())
print(Sum(2,3).calculate())
print(Multiply(2.00000000000,3.0).calculate())
