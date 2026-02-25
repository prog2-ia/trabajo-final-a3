# producto.py

class Producto:
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion):
        self.id = id
        self.titulo = titulo
        self.precio = precio
        self.vendedor = vendedor
        self.estado = estado
        self.stock = stock
        self.fecha_publicacion = fecha_publicacion

    def __str__(self):
        cadena = f'Producto: {self.titulo} | Precio: {self.precio} € | Stock: {self.stock}'

        return cadena

    def validar_precio(self):
        if self.precio <= 0:
            print('Precio no valido')
            return False
        else:
            print('Precio valido')
            return True

    def esta_disponible(self):
        if self.stock == 0:
            print('No hay stock disponible')
            return False
        else:
            print(f'Stock disponible: {self.stock} unidades de {self.titulo}')

  #  def reducir_stock(self): cuando se compre algún producto



