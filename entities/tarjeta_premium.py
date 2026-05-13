# tarjeta_premium.py
# Clase que representa una tarjeta premium de un usuario
class TarjetaPremium:
    # Constructor de la clase
    # codigo: identificador de la tarjeta
    # fecha_caducidad: fecha de caducidad de la tarjeta
    def __init__(self, codigo: str, fecha_caducidad: str, descuento: float = 0.10) -> None:

        if not codigo or codigo.strip() == '':
            raise ValueError('El código de la tarjeta es obligatorio.')

        if not fecha_caducidad or fecha_caducidad.strip() == '':
            raise ValueError('La fecha de la caducidad no puede estar vacía.')

        if descuento < 0 or descuento > 1:
            raise ValueError('El descuento debe estar entre 0 y 1.')

        self.codigo = codigo
        self.fecha_caducidad = fecha_caducidad
        self.descuento = descuento


    # Metodo especial para mostrar la información de la tarjeta al imprimirla
    def __str__(self) -> str:
        return f'Tarjeta Premium | Código: {self.codigo} | Fecha Caducidad: {self.fecha_caducidad} | Descuento: {self.descuento * 100}%'

    def aplicar_descuento(self, precio: float) -> float:
        return round(precio * (1 - self.descuento), 2)

    def esta_caducada(self, fecha_actual:str) -> bool:
        return fecha_actual > self.fecha_caducidad