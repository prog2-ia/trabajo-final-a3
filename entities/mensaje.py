# mesaje.py
from datetime import datetime

# Clase mensaje
class Mensaje:
    # Constructor de la clase
    # Se ejecuta cuando se crea un mensaje
    def __init__(self, autor, texto):
        #añadir excepciones aqui
        self.autor = autor
        self.texto = texto
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f'{self.autor.nombre} [{self.fecha}]: {self.texto}'
