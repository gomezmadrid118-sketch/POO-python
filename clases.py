class Perro:
    especie = 'Canis familiaris'

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f'{self.nombre} dice: ¡Guau!'


rex = Perro('Rex', 3)
luna = Perro('Luna', 5)

print(f'Especie de {rex.nombre}: {rex.especie}')
print(f'Especie de {luna.nombre}: {luna.especie}')

print(f'{rex.nombre} tiene {rex.edad} años.')
print(f'{luna.nombre} tiene {luna.edad} años.')

print(rex.ladrar())
print(luna.ladrar())