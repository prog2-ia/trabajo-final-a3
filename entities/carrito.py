# carrito.py

from entities.producto import Producto
from entities.persona import Persona

# Clase Carrito que representa la lista de compras de un comprador
class Carrito:
    # Constructor de la clase
    # comprador: objeto Persona o Pagar
    # lista_productos: lista de objetos Producto
    def __init__(self, comprador: Persona, lista_productos: list[Producto] = None) -> None:

        if not isinstance(comprador, Persona):
            raise TypeError('El comprador debe ser un objeto de tipo Persona.')

        self.comprador = comprador
        # Inicializamos la lista de productos como lista vacía si no se pasa nada
        if lista_productos is None:
            self.lista_productos = []
        else:
            self.lista_productos = lista_productos
    # Metodo para agregar un producto al carrito

    def agregar_producto(self, producto: Producto) -> bool:
        if not isinstance(producto, Producto):
            raise TypeError('Solo se pueden añadir objetos de tipo Producto al carrito.')

        if producto in self.lista_productos:
            raise ValueError('El producto ya está en el carrito.')
        # Añadimos un producto a la lista
        self.lista_productos.append(producto)
        return True

    # Metodo para eliminar todos los productos del carrito
    def eliminar_productos(self) -> bool:
        self.lista_productos.clear()
        return True

    # Metodo para calcular el total del carrito
    def calcular_total(self) -> float:
        total = 0.0
        # Sumamos el precio de todos los productos en la lista
        for producto in self.lista_productos:
            total += producto.precio
        return total

    # Sobrecarga de operadores
    # Metodo especial para saber la cantidad de productos del carrito
    def __len__(self) -> int:
        return len(self.lista_productos)

    # Metodo especial para añadir productos al carrito
    def __add__(self, otro: 'Carrito') -> 'Carrito':
        if not isinstance(otro, Carrito):
            raise TypeError('Solo se pueden sumar dos carritos.')

        if self.comprador != otro.comprador:
            raise ValueError('No se pueden sumar carritos de compradores distintos.')

        nuevo = Carrito(self.comprador)
        nuevo.lista_productos = self.lista_productos[:] + otro.lista_productos[:]
        return nuevo

    def eliminar_producto(self, producto: Producto) -> bool:
        if producto in self.lista_productos:
            self.lista_productos.remove(producto)
            return True

        raise ValueError('No se puede eliminar el producto porque no está en el carrito.')

    def contar_producto(self, producto: Producto) -> int:
        return self.lista_productos.count(producto)