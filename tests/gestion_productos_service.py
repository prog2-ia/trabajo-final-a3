# gestion_productos_service.py

# services/gestion_productos_service.py

from entities.producto_ropa import ProductoRopa
from entities.producto_electronico import ProductoElectronico
from entities.producto_coche import ProductoCoche


class GestionProductosService:

    def __init__(self, marketplace):
        self.marketplace = marketplace


    # LÓGICA

    def publicar_producto(self, producto):
        self.marketplace.registrar_producto(producto)

    def listar_productos(self):
        return self.marketplace.listar_productos()

    def comprar_producto(self, comprador, producto, cantidad):
        comprador.comprar(producto, cantidad)

    def buscar_por_titulo(self, texto):
        return self.marketplace.buscar_por_titulo(texto)

    def buscar_por_tipo(self, tipo):
        return self.marketplace.buscar_por_tipo(tipo)

    # CLI

    def publicar_producto_cli(self):
        print('\n--- Publicar producto ---')

        dni = input('DNI del vendedor: ')
        vendedor = self.marketplace.buscar_usuario_por_dni(dni)

        if vendedor is None:
            print('Usuario no encontrado.')
            return

        print('\nTipos de producto:')
        print('1. Ropa')
        print('2. Electrónico')
        print('3. Coche')
        tipo = input('Selecciona tipo: ')

        id_prod = input('ID del producto: ')
        titulo = input('Título: ')
        precio = float(input('Precio: '))
        estado = input('Estado (Nuevo/Seminuevo/Usado): ')
        stock = int(input('Stock: '))
        fecha = input('Fecha publicación: ')

        try:
            if tipo == '1':
                talla = input('Talla: ')
                material = input('Material: ')
                producto = ProductoRopa(id_prod, titulo, precio, vendedor, estado, stock, fecha, talla, material)

            elif tipo == '2':
                marca = input('Marca: ')
                modelo = input('Modelo: ')
                garantia = int(input('Garantía (años): '))
                producto = ProductoElectronico(id_prod, titulo, precio, vendedor, estado, stock, fecha, marca, modelo, garantia)

            elif tipo == '3':
                matricula = input('Matrícula: ')
                marca = input('Marca: ')
                ano = int(input('Año: '))
                combustible = input('Combustible: ')
                km = int(input('Kilómetros recorridos: '))
                producto = ProductoCoche(id_prod, titulo, precio, vendedor, estado, stock, fecha, matricula, marca, ano, combustible, km)

            else:
                print('Tipo no válido.')
                return

            self.publicar_producto(producto)
            print('Producto publicado correctamente.')

        except Exception as e:
            print('Error:', e)

    def listar_productos_cli(self):
        print('\n--- Lista de productos ---')
        productos = self.listar_productos()

        if not productos:
            print('No hay productos publicados.')
            return

        for p in productos:
            print(' -', p)

    def comprar_producto_cli(self):
        print('\n--- Comprar producto ---')

        dni = input('DNI del comprador: ')
        comprador = self.marketplace.buscar_usuario_por_dni(dni)

        if comprador is None:
            print('Usuario no encontrado.')
            return

        id_prod = input('ID del producto: ')
        try:
            producto = self.marketplace.buscar_producto(id_prod)
            cantidad = int(input('Cantidad: '))
            self.comprar_producto(comprador, producto, cantidad)
            print('Compra realizada correctamente.')
        except Exception as e:
            print('Error:', e)

    def buscar_por_titulo_cli(self):
        texto = input('\nTexto a buscar: ')
        resultados = self.buscar_por_titulo(texto)

        if not resultados:
            print('No se encontraron productos.')
            return

        print('\nResultados:')
        for p in resultados:
            print(' -', p)

    def buscar_por_tipo_cli(self):
        print('\n1. Ropa\n2. Electrónico\n3. Coche')
        tipo = input('Selecciona tipo: ')

        if tipo == '1':
            resultados = self.buscar_por_tipo(ProductoRopa)
        elif tipo == '2':
            resultados = self.buscar_por_tipo(ProductoElectronico)
        elif tipo == '3':
            resultados = self.buscar_por_tipo(ProductoCoche)
        else:
            print('Tipo no válido.')
            return

        if not resultados:
            print('No se encontraron productos.')
            return

        print('\nResultados:')
        for p in resultados:
            print(' -', p)