# estado_producto.py

class EstadoProducto:
    NUEVO = 'Nuevo'
    SEMINUEVO = 'Seminuevo'
    USADO = 'Usado'

    def __init__(self, estado):
        self.estado = estado

    # Añadir excepciones aquí

    def __str__(self):
        return f'Estado: {self.estado}'