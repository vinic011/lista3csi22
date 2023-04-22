class animal:
    def __init__(self) :
        self.bucho = True
        
    def comer(self):
        print("como para sobreviver")

class racional:
    def __init__(self) :
        self.mente = True
        
    def pensar(self):
        print("nao vejo só matéria, mas forma")
        
        
    
class homem(animal,racional):
    def __init__(self):
        animal.__init__(self)
        racional.__init__(self)
        
    def falar(self):
        print("sou carne, mas nao vivo segundo os desejos da carne, mas os do espírito")

h = homem()
h.comer()
h.pensar()
h.falar()
print(h.mente)
print(h.bucho)