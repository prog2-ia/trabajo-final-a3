#pagar.py
from persona import Persona
class Pagar(Persona):
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None, importe):
        super().__init__(dni, nombre, apellido, tarjeta_premium = None)
        self.importe = importe


