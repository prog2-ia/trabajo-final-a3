# tarjeta_premium.py

class Tarjeta:
    def __init__(self, codigo, fecha_caducidad):
        self.codigo = codigo
        self.fecha_caducidad = fecha_caducidad

    def __str__(self):
        return (f'Tarjeta Premium: , Código: {self.codigo}, Fecha Caducidad: {self.fecha_caducidad}')

