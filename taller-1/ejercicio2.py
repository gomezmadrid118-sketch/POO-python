# Este ejercicio engloba el punto 4

class Mascota():
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        return f'{self.nombre} está comiendo'
    
class Perro(Mascota):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
    def ladrar(self):
        return f'{self.nombre}: "¡Guau!"'
    
class Gato(Mascota):
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def maullar(self):
        return f'{self.nombre}: "¡Miau!"'
    
perro = Perro('Firu', 'Doberman')
gato = Gato('Luis', 'Naranja')

print(perro.comer())
print(gato.comer())

print(perro.ladrar())
print(gato.maullar())