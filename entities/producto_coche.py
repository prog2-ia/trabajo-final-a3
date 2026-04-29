# producto_coche.py

# Importamos la clase base Producto
from entities.producto import Producto
# Clase ProductoCoche que hereda de Producto
class ProductoCoche(Producto):
    # Constructor de la clase
    # Añade atributos específicos de coches: matrícula, marca, año, tipo de combustible, kilómetros recorridos
    def __init__(self, id: str, titulo: str, precio: float, vendedor: object, estado: str, stock: int, fecha_publicacion: str,
                 matricula: str, marca: str, ano: int, combustible: str, kilometros_recorridos: int) -> None:
        # Llamamos al constructor de la clase padre (Producto)
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)
        # Atributos propios de ProductoCoche
        self.matricula = matricula
        self.marca = marca
        self.ano = ano
        self.combustible = combustible
        self.kilometros_recorridos = kilometros_recorridos

    # Metodo especial para mostrar información del producto al imprimirlo
    def __str__(self) -> str:
        # Llamamos al __str__ de la clase padre y añadimos los atributos propios
        return (f'{super().__str__()} Marca: {self.marca}, Año: {self.ano}, '
                f'Km: {self.kilometros_recorridos}, Combustible: {self.combustible}')
