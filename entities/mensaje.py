# mesaje.py

# Clase mensaje
class Mensaje:
    # Constructor de la clase
    # Se ejecuta cuando se crea un mensaje
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto

    def __str__(self):
        return f'{self.autor.nombre}: {self.texto}'
