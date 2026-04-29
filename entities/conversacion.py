# conversacion.py

# Importamos la clase Mensaje desde el archivo mensaje.py
from mensaje import Mensaje

# Clase Conversacion
class Conversacion:
    # Constructor de la clase
    # Se ejecuta cuando se crea una conversacion
    def __init__(self, usuario1: object, usuario2: object) -> None:
        self.usuarios = (usuario1, usuario2)
        self.mensajes: list[Mensaje] = []

    # Metodo para añadir mensajes
    def agregar_mensaje(self, autor: object, texto: str) -> bool:
        mensaje = Mensaje(autor, texto)
        self.mensajes.append(mensaje)
        # Añadir excepciones

        # Devolver historial de mensajes
    def obtener_historial(self) -> list[Mensaje]:
        return self.mensajes[:]

    # Representación opcional de la conversación
    def __str__(self) -> str:
        return f'Conversación entre {self.usuarios[0].nombre} y {self.usuarios[1].nombre}'
