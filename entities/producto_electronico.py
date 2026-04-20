# producto_electrónico.py

# Importamos la clase base Producto
from entities.producto import Producto
# Clase ProductoElectronico que hereda de Producto
class ProductoElectronico(Producto):
    # Constructor de la clase
    # Añade atributos específicos de productos electrónicos
    # marca, modelo y garantía
    def __init__(self, id, titulo, precio, vendedor, estado, stock, fecha_publicacion, marca, modelo, garantia):
        # Llamamos al constructor de la clase padre para inicializar los atributos heredados
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        # Atributos propios de ProductoElectronico
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia  # en años
    # Metodo especial para mostrar la información del producto al imprimirlo
    def __str__(self):
        # Llamamos al __str__ de la clase padre y añadimos los atributos específicos
        return f'{super().__str__()} Marca: {self.marca}, Modelo: {self.modelo}, Garantía: {self.garantia} años'
