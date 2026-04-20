# pagar_tarjeta.py

# Importamos la clase Pagar
from entities.pagar import Pagar
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

    # Sobreescribir comprar
    def comprar(self, producto, cantidad):
        total = producto.precio * cantidad

        if self.saldo < total:
            print('Saldo insuficiente en la tarjeta')
            return False

        if producto.reducir_stock(cantidad):
            self.saldo -= total
            print(f'{self.nombre} compró {producto.titulo} con tarjeta')
            return True
