# estado_producto.py

class EstadoProductos:
    NUEVO = 'Nuevo'
    SEMINUEVO = 'Seminuevo'
    USADO = 'Usado'

    def __init__(self, estado):
        self.estado = estado
