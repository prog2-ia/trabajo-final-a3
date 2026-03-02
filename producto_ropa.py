# producto_ropa.py
from producto import Producto

class ProductoRopa(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, talla, material):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.talla = talla
        self.material = material

