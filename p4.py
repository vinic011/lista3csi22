class Multiplicator:
    name = "I can multiply"
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    @classmethod 
    def who_am_i(cls):
        return print(cls.name)
    
    @staticmethod
    def static_multiply(x,y):
        return x*y
    
    def multiply(self):
        mul = 0
        for i in range(int(self.b)):
            mul = mul+self.a
        return mul
    
m = Multiplicator(5,6)
print(m.multiply())
print(m.static_multiply(3,5))
m.who_am_i()

    