# pagar_efectivo.py

from pagar import Pagar

class PagarEfectivo(Pagar):
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None, importe, ):
        super.__init__(dni, nombre, apellido, tarjeta_premium = None, importe)
