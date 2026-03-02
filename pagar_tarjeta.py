# pagar_tarjeta.py

from pagar import Pagar

class PagarTarjeta(Pagar):
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None, importe, saldo):
        super().__init__(dni, nombre, apellido, tarjeta_premium = None, importe)
        self.saldo = saldo
