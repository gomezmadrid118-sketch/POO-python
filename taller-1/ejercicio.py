# Este ejercicio engloba desde el punto 1 al 3

class Mascota():
    reino = 'Animal'
    total_mascotas = 0
    nombre = None
    _dueno = None
    __edad = None
    
    def __init__(self, nombre, especie, dueno, edad):
        self.nombre = nombre
        self.especie = especie
        self._dueno = dueno
        self.__edad = edad
        Mascota.total_mascotas += 1
    
    def presentarse(self):
        return f'Hola mi nombre es {self.nombre} y soy un(a) {self.especie}'


    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        if(edad >= 0):
            self.edad = edad
        else:
            print('Edad inválida')
            

perro = Mascota('Manchas', 'Perro', 'Luis', 17)
elefante = Mascota('Dumbo', 'Elefante', 'Paula', 12)
tigre = Mascota('Colmillo', 'Tigre', 'Ninguno', 8)

print(perro.presentarse())
print(elefante.presentarse())


print(tigre.nombre)
print(perro.nombre)
print(elefante.nombre)

print(tigre.reino)
print(perro.reino)

print(Mascota.total_mascotas)

gato = Mascota('Nieve', 'Gato', 'Karen', 2)

print(gato.nombre)
print(gato._dueno)
# print(gato.__edad) lo dejo comentado para evitar problemas al compilar

gato.setEdad(-5)
gato.setEdad(4)