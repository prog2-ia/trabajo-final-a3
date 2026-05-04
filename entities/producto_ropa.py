# producto_ropa.py
# Importamos la clase base Producto
from entities.producto import Producto
# Clase ProductoRopa que hereda de Producto
class ProductoRopa(Producto):
    # Constructor de la clase
    # Añade atributos específicos de la ropa: talla y material
    def __init__(self, id: str, titulo: str, precio: float, vendedor: object, estado: str, stock: int, fecha_publicacion: str, talla: str, material: str) -> None:
        # Llamamos al constructor de la clase padre (Producto)
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)

        if not talla or talla.strip() == '':
            raise ValueError('La talla no puede estar vacía.')

        if not material or material.strip() == '':
            raise ValueError('El material no puede estar vacío.')

        # Atributos propios de ProductoRopa
        self.talla = talla
        self.material = material

    # Metodo especial para mostrar información del producto al imprimirlo
    def __str__(self) -> str:
        # Llamamos al __str__ de la clase padre y añadimos los atributos propios
        return f'{super().__str__()} | Talla: {self.talla} | Material: {self.material}'
