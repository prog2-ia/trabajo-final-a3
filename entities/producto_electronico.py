# producto_electrónico.py

# Importamos la clase base Producto
from entities.producto import Producto
# Clase ProductoElectronico que hereda de Producto
class ProductoElectronico(Producto):
    # Constructor de la clase
    # Añade atributos específicos de productos electrónicos
    def __init__(self, id: str, titulo: str, precio: float, vendedor: object, estado: str, stock: int, fecha_publicacion: str, marca: str, modelo: str, garantia: int) -> None:
        # Llamamos al constructor de la clase padre para inicializar los atributos heredados
        super().__init__(id, titulo, precio, vendedor, estado, stock, fecha_publicacion)

        if not marca or marca.strip() == '':
            raise ValueError('La marca no puede estar vacía.')

        if not modelo or modelo.strip() == '':
            raise ValueError('El modelo no puede estar vacío.')

        if garantia < 0:
            raise ValueError('La garantía no puede ser negativa.')

        # Atributos propios de ProductoElectronico
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia

    # Metodo especial para mostrar la información del producto al imprimirlo
    def __str__(self) -> str:
        # Llamamos al __str__ de la clase padre y añadimos los atributos específicos
        return f'{super().__str__()} | Marca: {self.marca} | Modelo: {self.modelo} | Garantía: {self.garantia} años'