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
        # Añadir excepciones

        # Devolver historial de mensajes
    def obtener_historial(self):
        return self.mensajes[:]

    # Representación opcional de la conversación
    def __str__(self):
        return f'Conversación entre {self.usuarios[0].nombre} y {self.usuarios[1].nombre}'
#