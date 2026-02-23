# producto.py

class Producto:
    def __init__(self, id, nombre, precio, vendedor, estado, stock, fecha_publicacion):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.vendedor = vendedor
        self.estado = estado
        self.stock = stock
        self.fecha_publicacion = fecha_publicacion

    def __str__(self):
        cadena = f'Producto: {self.nombre} | Precio: {self.precio} € | Stock: {self.stock}'

        return cadena

    def validar_precio(self)
        if self.precio <= 0:
            print('Precio no valido')
            return False

    #def esta_disponible(self, ):
    #def reducir_stock(self):

