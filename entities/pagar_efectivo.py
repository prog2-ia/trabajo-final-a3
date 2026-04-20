# pagar_efectivo.py

# Importamos la clase Pagar
from entities.pagar import Pagar
# Definimos la clase PagarEfectivo que hereda de Pagar
class PagarEfectivo(Pagar):
    # Constructor de la clase
    # Recibe los datos de la persona y el importe disponible
    def __init__(self, dni, nombre, apellido, importe, tarjeta_premium=None):
        # Llamamos al constructor de la clase padre (Pagar)
        # para inicializar los atributos heredados
        super().__init__(dni, nombre, apellido, importe, tarjeta_premium)
