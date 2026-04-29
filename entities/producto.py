# producto.py

# Importamos la clase Publicacion desde el archivo publicacion.py
from publicacion import Publicacion

# Definición de la clase Producto
class Producto(Publicacion):

    # Constructor de la clase.
    # Se ejecuta cuando se crea un nuevo producto.
    def __init__(self, id: str, titulo: str, precio: float, vendedor: object, estado: str, stock: int, fecha_publicacion: str) -> None:
        self._id = id
        self._titulo = titulo
        self._precio = precio
        self._vendedor = vendedor
        self._estado = estado
        self._stock = stock
        self._fecha_publicacion = fecha_publicacion

    # Implementación del metodo abstracto
    def mostrar_info(self) -> str:
        return str(self)

    # Implementación del metodo abstracto
    def calcular_precio_final(self) -> float:
        return self._precio


    # Metodo de clase que permite crear un producto a partir de un diccionario
    @classmethod
    def desde_diccionario(cls, datos: dict, vendedor: object) -> 'Producto':
        return cls(
            datos['id'],
            datos['titulo'],
            datos['precio'],
            vendedor,
            datos['estado'],
            datos['stock'],
            datos['fecha_publicacion']
        )


    # Metodo especial que define cómo se muestra el producto al imprimirlo
    def __str__(self) -> str:
        return f'Producto: {self.titulo} | Precio: {self.precio} € | Stock: {self.stock}'


    # Getter del precio (permite acceder a precio como producto.precio)
    @property
    def precio(self) -> float:
        return self._precio


    # Setter del precio (permite modificarlo con validación)
    @precio.setter
    def precio(self, valor):
        if valor > 0:                   # Validación: el precio no puede ser negativo o 0
            self._precio = valor


    # Getter del stock
    @property
    def stock(self) -> int:
        return self._stock


    # Setter del stock con validación
    @stock.setter
    def stock(self, valor: int) -> None:
        if valor >= 0:
            self._stock = valor


    # Getter del título (solo lectura)
    @property
    def titulo(self) -> str:
        return self._titulo


    # Getter del id (solo lectura)
    @property
    def id(self) -> str:
        return self._id

    # Getter de fecha_publicación (solo lectura)
    @property
    def fecha_publicacion(self) -> str:
        return self._fecha_publicacion


    ## Metodo para validar si el precio es correcto
    def validar_precio(self) -> bool:
        return self.precio > 0

    # Metodo para comprobar si el producto tiene stock disponible
    def esta_disponible(self) -> bool:
        return self.stock > 0


    # Metodo para reducir el stock cuando alguien compra el producto
    def reducir_stock(self, cantidad: int) -> bool:

        # Validamos que la cantidad sea mayor que 0
        if cantidad <= 0:
           # print('Cantidad no válida')
            return False

        # Comprobamos si hay suficiente stock
        if self.stock < cantidad:
           # print('No hay suficiente stock disponible')
            return False

        #  si esta correcto, reducimos el stock

           # print('Cantidad reducida')
        self.stock -= cantidad
        return True
