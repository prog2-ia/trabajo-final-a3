# producto_ropa.py
from producto import Producto

class ProductoRopa(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, talla, material):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.talla = talla
        self.material = material

    def __str__(self):
        return f'{super().__str__()} Talla: {self.talla}, Material: {self.material}'

