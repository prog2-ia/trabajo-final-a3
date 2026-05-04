# producto.py

# Importamos la clase Publicacion desde el archivo publicacion.py
from entities.publicacion import Publicacion
from entities.excepciones import StockError, PrecioInvalidoError

# Definición de la clase Producto
class Producto(Publicacion):

    # Constructor de la clase.
    # Se ejecuta cuando se crea un nuevo producto.
    def __init__(self, id: str, titulo: str, precio: float, vendedor: object, estado: str, stock: int, fecha_publicacion: str) -> None:

        if not id or id.strip() == '':
            raise ValueError('El id no puede estar vacío.')

        if not titulo or titulo.strip() == '':
            raise ValueError('El título no puede estar vacío.')

        if precio <= 0:
            raise PrecioInvalidoError('El precio no puede ser negativo.')

        if vendedor is None:
            raise ValueError('El vendedor no puede ser None.')

        if not estado or estado.strip() == '':
            raise ValueError('El estado no puede estar vacío.')

        if stock < 0:
            raise ValueError('El stock no puede ser negativo.')

        if not fecha_publicacion or fecha_publicacion.strip() == '':
            raise   ValueError('La fecha de publicación no puede estar vacía.')

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

        if not isinstance(datos, dict):
            raise TypeError('Los datos del producto deben estar en un diccionario.')

        claves = ['id', 'titulo', 'precio', 'estado', 'stock', 'fecha_publicacion']
        for clave in claves:
            if clave not in datos:
                raise KeyError(f'Falta la clave: {clave} en los datos del producto.')

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
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise PrecioInvalidoError('La precio no puede ser negativo.')
        self._precio = valor


    # Getter del stock
    @property
    def stock(self) -> int:
        return self._stock


    # Setter del stock con validación
    @stock.setter
    def stock(self, valor: int) -> None:
        if valor < 0:
            raise ValueError('La stock no puede ser negativo.')
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
           raise ValueError('La cantidad no puede ser negativa.')

        # Comprobamos si hay suficiente stock
        if self.stock < cantidad:
           raise StockError('No hay suficiente stock disponible.')

        self.stock -= cantidad
        return True

    def es_del_vendedor(self, persona: object) -> bool:
        return self._vendedor == persona

    def aumentar_stock(self, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError('La cantidad no puede ser negativa.')
        self.stock += cantidad
        return True

