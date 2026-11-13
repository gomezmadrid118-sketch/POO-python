# Este ejercicio engloba el punto 5

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre}: '¡Guau!'"

class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre}: '¡Miau!'"

class Vaca(Animal):
    def hacer_sonido(self):
        return f"{self.nombre}: '¡Muuu!'"

print("--- Recorriendo la lista de animales ---")
animales = [
    Perro("Firulais"),
    Gato("Michi"),
    Vaca("Lola")
]

for animal in animales:
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

print("\n--- Intentando instanciar la clase abstracta Animal ---")

try:

    animal = Animal("Genérico")
except TypeError as e:
    print(f"¡Error capturado exitosamente!\nDetalle: {e}")