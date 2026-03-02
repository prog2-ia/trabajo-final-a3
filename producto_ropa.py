# producto_ropa.py

class ProductoRopa(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, talla, material):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.talla = talla
        self.material = material

