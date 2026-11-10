class Animal:
    hogar = 'Planeta tierra'

    def __init__(self, especie, habitad):
        self.especie = especie
        self.habitad = habitad

    def respirar(self):
        return f'{self.nombre} ah respirado'


perro = Animal('Perro', 'Terrestre')
pajaro = Animal('Pajaro', 'Terrestre')

print(f'El {perro.especie} vive en {perro.hogar}')
print(f'El {pajaro.especie} vive en {pajaro.hogar}')

print(f'El {perro.especie} es del habitad {perro.habitad}')
print(f'El {pajaro.especie} es del habitad {pajaro.habitad}')

print(perro.respirar())
print(pajaro.respirar())