# estado_producto.py

class EstadoProducto:
    NUEVO = 'Nuevo'
    SEMINUEVO = 'Seminuevo'
    USADO = 'Usado'

    def __init__(self, estado: str) -> None:
        if estado not in (self.NUEVO, self.SEMINUEVO, self.USADO):
            raise ValueError(f'{estado} no válido. Debe ser: '
                             f'{self.NUEVO}, {self.SEMINUEVO}, {self.USADO}')

        self.estado = estado


    def __str__(self) -> str:
        return f'Estado: {self.estado}'
