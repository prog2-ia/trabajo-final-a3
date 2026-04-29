# tarjeta_premium.py
# Clase que representa una tarjeta premium de un usuario
class TarjetaPremium:
    # Constructor de la clase
    # codigo: identificador de la tarjeta
    # fecha_caducidad: fecha de caducidad de la tarjeta
    def __init__(self, codigo: str, fecha_caducidad: str, descuento: float = 0.10) -> None:
        self.codigo = codigo
        self.fecha_caducidad = fecha_caducidad
        self.descuento = descuento
        #excepciones (añadir en este apartado)

    # Metodo especial para mostrar la información de la tarjeta al imprimirla
    def __str__(self) -> str:
        return f'Tarjeta Premium: Código: {self.codigo}, Fecha Caducidad: {self.fecha_caducidad}, Descuento: {self.descuento * 100}%'

    def aplicar_descuento(self, precio: float) -> float:
        return round(precio * (1 - self.descuento), 2)
