# producto_electrónico.py
from producto import Producto
class ProductoElectronico(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, marca, modelo, garantia):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.modelo = modelo
        self.marca = marca
        self.garantia = garantia

