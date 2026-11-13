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

# Clase 2
class Contador:
    total = 0 # de clase
    def __init__(self):
        Contador.total += 1 # modifica el valor compartido
        self.numero = Contador.total # de instancia

a = Contador()
b = Contador()
print(a.numero, b.numero, Contador.total) # 1 2 2


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # privado
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto
    def retirar(self, monto):
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto
    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.consultar_saldo()) # 1500
# print(cuenta.__saldo) # AttributeError


class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius # pasa por el setter
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Por debajo del cero absoluto")
        self._celsius = valor
    @property
    def fahrenheit(self): # propiedad calculada, solo lectura
        return self._celsius * 9 / 5 + 32

t = Temperatura(25)
print(t.fahrenheit) # 77.0
t.celsius = 30 # usa el setter con validación

