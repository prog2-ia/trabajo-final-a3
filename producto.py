# producto.py

# Importamos la clase Publicacion desde el archivo publicacion.py
from publicacion import Publicacion

# Definición de la clase Producto
class Producto(Publicacion):

    # Constructor de la clase.
    # Se ejecuta cuando se crea un nuevo producto.
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion):
        self._id = id                        # Identificador único del producto
        self._titulo = titulo                # Título o nombre del producto
        self._precio = precio                # Precio del producto
        self._vendedor = vendedor            # Persona que vende el producto
        self._estado = estado                # Estado del producto (nuevo, usado, etc.)
        self._stock = stock                  # Cantidad disponible del producto
        self._fecha_publicacion = fecha_publicacion  # Fecha en la que se publicó

    # Implementación del metodo abstracto
    def mostrar_info(self):
        return str(self)

    # Implementación del metodo abstracto
    def calcular_precio_final(self):
        return self._precio


    # Metodo de clase que permite crear un producto a partir de un diccionario
    @classmethod
    def desde_diccionario(cls, datos, vendedor):
        return cls(
            datos['id'],                # ID del producto
            datos['titulo'],            # Título del producto
            datos['precio'],            # Precio
            vendedor,                   # Persona que lo vende
            datos['estado'],            # Estado del producto
            datos['stock'],             # Stock disponible
            datos['fecha_publicacion']  # Fecha de publicación
        )


    # Metodo especial que define cómo se muestra el producto al imprimirlo
    def __str__(self):
        cadena = f'Producto: {self.titulo} | Precio: {self.precio} € | Stock: {self.stock}'
        return cadena


    # Getter del precio (permite acceder a precio como producto.precio)
    @property
    def precio(self):
        return self._precio


    # Setter del precio (permite modificarlo con validación)
    @precio.setter
    def precio(self, valor):
        if valor <= 0:                   # Validación: el precio no puede ser negativo o 0
            print("Precio no válido")
        else:
            self._precio = valor


    # Getter del stock
    @property
    def stock(self):
        return self._stock


    # Setter del stock con validación
    @stock.setter
    def stock(self, valor):
        if valor < 0:                    # El stock no puede ser negativo
            print("Stock no válido")
        else:
            self._stock = valor


    # Getter del título (solo lectura)
    @property
    def titulo(self):
        return self._titulo


    # Getter del id (solo lectura)
    @property
    def id(self):
        return self._id

    # Getter de fecha_publicación (solo lectura)
    @property
    def fecha_publicacion(self):
        return self._fecha_publicacion


    # Metodo para validar si el precio es correcto
    def validar_precio(self):
        if self.precio <= 0:
            print('Precio no valido')
            return False
        else:
            print('Precio valido')
            return True


    # Metodo para comprobar si el producto tiene stock disponible
    def esta_disponible(self):
        if self.stock == 0:
            print('No hay stock disponible')
            return False
        else:
            print(f'Stock disponible: {self.stock} unidades de {self.titulo}')
            return True


    # Metodo para reducir el stock cuando alguien compra el producto
    def reducir_stock(self, cantidad):

        # Validamos que la cantidad sea mayor que 0
        if cantidad <= 0:
            print('Cantidad no válida')
            return False

        # Comprobamos si hay suficiente stock
        elif self.stock < cantidad:
            print('No hay suficiente stock disponible')
            return False

        #  si esta correcto, reducimos el stock
        else:
            print('Cantidad reducida')
            self.stock -= cantidad
            return True
