# producto_ropa.py

# Importamos la clase base Producto
from producto import Producto
# Clase ProductoRopa que hereda de Producto
class ProductoRopa(Producto):
    # Constructor de la clase
    # Añade atributos específicos de la ropa: talla y material
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, talla, material):
        # Llamamos al constructor de la clase padre (Producto)
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        # Atributos propios de ProductoRopa
        self.talla = talla  # Ej: S, M, L, XL
        self.material = material  # Ej: algodón, poliéster

    # Metodo especial para mostrar información del producto al imprimirlo
    def __str__(self):
        # Llamamos al __str__ de la clase padre y añadimos los atributos propios
        return f'{super().__str__()} Talla: {self.talla}, Material: {self.material}'
