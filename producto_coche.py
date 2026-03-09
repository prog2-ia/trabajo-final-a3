# producto_coche.py
from producto import Producto

class ProductoCoche(Producto):
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, matricula, marca, ano, combustible, kilometros_recorridos):
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.ano = ano
        self.combustible = combustible

    def __str__(self):
        return f'{super().__str__()} Marca: {self.marca}, Año: {self.ano}, Km: {self.kilometros_recorridos}'