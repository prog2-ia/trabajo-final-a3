# pagar.py

# Importamos la clase Persona
from persona import Persona


# Definimos la clase Pagar que hereda de Persona
class Pagar(Persona):

    # Constructor de la clase
    # Añadimos el atributo importe (dinero disponible para pagar)
    def __init__(self, dni, nombre, apellido, importe, tarjeta_premium=None):

        # Llamamos al constructor de la clase padre (Persona)
        # para inicializar dni, nombre, apellido y tarjeta premium
        super().__init__(dni, nombre, apellido, tarjeta_premium)

        # Nuevo atributo propio de la clase Pagar
        # Representa el dinero disponible de la persona
        self.importe = importe


