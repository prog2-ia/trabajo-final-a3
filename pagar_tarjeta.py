# pagar_tarjeta.py

# Importamos la clase Pagar
from pagar import Pagar
# Clase PagarTarjeta que hereda de Pagar
class PagarTarjeta(Pagar):
    # Constructor de la clase
    # Añade un atributo saldo de la tarjeta
    def __init__(self, dni, nombre, apellido, importe, saldo, tarjeta_premium=None):
        # Llamamos al constructor de la clase padre (Pagar)
        # Inicializa dni, nombre, apellido, tarjeta_premium e importe
        super().__init__(dni, nombre, apellido, importe, tarjeta_premium)
        # Nuevo atributo propio de PagarTarjeta
        # Representa el saldo disponible en la tarjeta
        self.saldo = saldo
