# tarjeta_premium.py
# Clase que representa una tarjeta premium de un usuario
class Tarjeta:
    # Constructor de la clase
    # codigo: identificador de la tarjeta
    # fecha_caducidad: fecha de caducidad de la tarjeta
    def __init__(self, codigo, fecha_caducidad, descuento = 0.10):
        self.codigo = codigo
        self.fecha_caducidad = fecha_caducidad
        self.descuento = descuento # 10% por defecto

    # Metodo especial para mostrar la información de la tarjeta al imprimirla
    def __str__(self):
        return f'Tarjeta Premium: Código: {self.codigo}, Fecha Caducidad: {self.fecha_caducidad}, Descuento: {self.descuento * 100}%'

    def aplicar_descuento(self, precio):
        return round(precio * (1 - self.descuento), 2)

