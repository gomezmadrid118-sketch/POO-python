class Vehiculo:
    tieneMotor = True

    def __init__(self, tipo, velocidad, superficie):
        self.tipo = tipo
        self.velocidad = velocidad
        self.superficie = superficie

    def arrancar(self):
        return f"El/La {self.tipo} ha arrancado."


avion = Vehiculo('Avion', 250, 'Aereo')
camioneta = Vehiculo('Camioneta', 150, 'Terrestre')

print(f'El {avion.tipo} tiene motor: {avion.tieneMotor}')
print(f'La {camioneta.tipo} tiene motor: {camioneta.tieneMotor}')

print(f'El {avion.tipo} va a máximo {avion.velocidad} km por hora')
print(f'La {camioneta.tipo} va a máximo {camioneta.velocidad} km por hora')

print(avion.arrancar())
print(camioneta.arrancar())