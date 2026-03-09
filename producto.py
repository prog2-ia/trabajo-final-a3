# producto.py

class Producto:
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion):
        self._id = id
        self._titulo = titulo
        self._precio = precio
        self._vendedor = vendedor
        self._estado = estado
        self._stock = stock
        self._fecha_publicacion = fecha_publicacion

    @classmethod
    def desde_diccionario(cls, datos, vendedor):
        return cls(
            datos['id'],
            datos['titulo'],
            datos['precio'],
            vendedor,
            datos['estado'],
            datos['stock'],
            datos['fecha_publicacion']
        )

    def __str__(self):
        cadena = f'Producto: {self.titulo} | Precio: {self.precio} € | Stock: {self.stock}'
        return cadena

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            print("Precio no válido")
        else:
            self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            print("Stock no válido")
        else:
            self._stock = valor

    @property
    def titulo(self):
        return self._titulo

    @property
    def id(self):
        return self._id

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
            return True

    def reducir_stock(self, cantidad):    #cuando se compre algún producto
        if cantidad <= 0:
            print('Cantidad no válida')
            return False
        elif self.stock < cantidad:
            print('No hay suficiente stock disponible')
            return False
        else:
            print('Cantidad reducida')
            self.stock -= cantidad
            return True