# producto_electrónico.py
from producto import Producto

class ProductoElectronico(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, marca, modelo, garantia):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.modelo = modelo
        self.marca = marca
        self.garantia = garantia


    def __str__(self):
        return f'{super().__str__()} Marca: {self.marca}, Modelo: {self.modelo}, Garantía: {self.garantia} años'

