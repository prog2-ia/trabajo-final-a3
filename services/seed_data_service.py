# services/seed_data_service.py

from entities.producto_ropa import ProductoRopa
from entities.producto_electronico import ProductoElectronico
from entities.producto_coche import ProductoCoche


class SeedDataService:

    def __init__(self, productos_service, usuarios_service):
        self.productos_service = productos_service
        self.usuarios_service = usuarios_service

    def cargar_datos_demo(self):
        # Usuarios demo
        u1 = self.usuarios_service.registrar_usuario('11111111H', 'Carlos', 'García')
        u2 = self.usuarios_service.registrar_usuario('22222222J', 'Lucía', 'Martínez')
        u3 = self.usuarios_service.registrar_usuario('33333333P', 'Pedro', 'Rimert')

        # Productos demo
        p1 = ProductoRopa('R001', 'Camiseta Oversize', 15.99, u1, 'Nuevo', 10, '15-02-2025', 'M', 'Algodón')
        p2 = ProductoElectronico('E001', 'Auriculares Bluetooth', 29.99, u2, 'Seminuevo', 5, '10-02-2025', 'Sony', 'WH-CH510', 2)
        p3 = ProductoCoche('C001', 'Seat Ibiza', 3500, u3, 'Usado', 1, '01-01-2025', '1234ABC', 'Seat', 2012, 'Gasolina', 145000)

        self.productos_service.publicar_producto(p1)
        self.productos_service.publicar_producto(p2)
        self.productos_service.publicar_producto(p3)

