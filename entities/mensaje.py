# mesaje.py
from datetime import datetime

# Clase mensaje
class Mensaje:
    # Constructor de la clase
    # Se ejecuta cuando se crea un mensaje
    def __init__(self, autor: object, texto: str) -> None:
        if autor is None:
            raise TypeError('Debe haber un autor para enviar un mensaje.')

        if not texto or texto.strip() == '':
            raise ValueError('Debe haber un texto para enviar un mensaje.')

        #añadir excepciones aqui
        self.autor = autor
        self.texto = texto
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self) -> str:
        return f'{self.autor.nombre} [{self.fecha}]: {self.texto}'
