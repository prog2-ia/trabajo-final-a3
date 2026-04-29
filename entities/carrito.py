# carrito.py

# Clase Carrito que representa la lista de compras de un comprador
class Carrito:
    # Constructor de la clase
    # comprador: objeto Persona o Pagar
    # lista_productos: lista de objetos Producto
    def __init__(self, comprador: Persona, lista_productos: list[Producto] = None) -> None:
        self.comprador = comprador
        # Inicializamos la lista de productos como lista vacía si no se pasa nada
        if lista_productos is None:
            self.lista_productos = []
        else:
            self.lista_productos = lista_productos
    # Metodo para agregar un producto al carrito

    def agregar_producto(self, producto: Producto) -> bool:
        # Añadimos un producto a la lista
        self.lista_productos.append(producto)
        #f'Producto {producto.titulo} agregado al carrito'
        return True

    # Metodo para eliminar todos los productos del carrito
    def eliminar_productos(self) -> bool:
        self.lista_productos.clear()
        #print('Carrito vaciado')
        return True

    # Metodo para calcular el total del carrito
    def calcular_total(self) -> float:
        total = 0
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
        nuevo = Carrito(self.comprador)
        nuevo.lista_productos = self.lista_productos[:] + otro.lista_productos[:]
        return nuevo

