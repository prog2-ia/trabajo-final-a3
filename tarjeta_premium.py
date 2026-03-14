# tarjeta_premium.py
# Clase que representa una tarjeta premium de un usuario
class Tarjeta:
    # Constructor de la clase
    # codigo: identificador de la tarjeta
    # fecha_caducidad: fecha de caducidad de la tarjeta
    def __init__(self, codigo, fecha_caducidad):
        self.codigo = codigo
        self.fecha_caducidad = fecha_caducidad

    # Metodo especial para mostrar la información de la tarjeta al imprimirla
    def __str__(self):
        return f'Tarjeta Premium: Código: {self.codigo}, Fecha Caducidad: {self.fecha_caducidad}'

