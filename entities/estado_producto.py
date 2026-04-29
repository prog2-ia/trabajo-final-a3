# estado_producto.py

class EstadoProducto:
    NUEVO = 'Nuevo'
    SEMINUEVO = 'Seminuevo'
    USADO = 'Usado'

    def __init__(self, estado: str) -> None:
        self.estado = estado

    # Añadir excepciones aquí

    def __str__(self) -> str:
        return f'Estado: {self.estado}'
#