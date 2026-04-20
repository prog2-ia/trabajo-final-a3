# conversacion.py

# Importamos la clase Mensaje desde el archivo mensaje.py
from mensaje import Mensaje

# Clase Conversacion
class Conversacion:
    # Constructor de la clase
    # Se ejecuta cuando se crea una conversacion
    def __init__(self, usuario1, usuario2):
        self.usuarios = (usuario1, usuario2)
        self.mensajes = []

    # Metodo para añadir mensajes
    def agregar_mensaje(self, autor, texto):
        mensaje = Mensaje(autor, texto)
        self.mensajes.append(mensaje)