# market_place.py

import random

# Importamos las clases necesarias del proyecto
from persona import Persona
from tarjeta_premium import Tarjeta
from producto import Producto
from pagar import Pagar
from pagar_tarjeta import PagarTarjeta
from pagar_efectivo import PagarEfectivo
from carrito import Carrito
from conversacion import Conversacion
from mensaje import Mensaje
from producto_ropa import ProductoRopa
from producto_coche import ProductoCoche
from producto_electronico import ProductoElectronico


#FUNCIONES PARA GENERAR DATOS ALEATORIOS
#VALIDACIÓN DNI

def validar_dni(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    numero = int(dni[:-1])       # Parte numérica del DNI
    letra = dni[-1].upper()      # Letra del DNI

    letra_correcta = letras[numero % 23]

    return letra == letra_correcta

# Genera un DNI aleatorio (8 números + 1 letra)
# def generar_dni():
#     letra_aleatoria = chr(random.randint(65, 90))  # Letra mayúscula aleatoria
#     numeros = random.randint(11111111,99999999)    # Número de 8 cifras
#     dni = str(numeros) + letra_aleatoria           # Unimos número y letra
#
#     return dni

def generar_dni():
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    numero = random.randint(11111111, 99999999)
    letra = letras[numero % 23]

    return str(numero) + letra



# Devuelve un nombre aleatorio de una lista
def generar_nombre():
    nombres = [
        'Carlos', 'Lucía', 'María', 'Pedro', 'Ana',
        'Javier', 'Marta', 'Sofía', 'Diego', 'Elena',
        'Raúl', 'Nohelia', 'Iván', 'Laura', 'Miguel'
    ]

    return random.choice(nombres)  # Selecciona un nombre al azar


# Devuelve un apellido aleatorio de una lista
def generar_apellido():
    apellidos = [
        'García', 'López', 'Martínez', 'Sánchez',
        'Pérez', 'Gómez', 'Ruiz', 'Fernández',
        'Torres', 'Díaz', 'Morales', 'Romero'
    ]

    return random.choice(apellidos)  # Selecciona un apellido al azar


#CLASE MARKETPLACE

class Marketplace:
    def __init__(self):
        self.productos = []  # Lista donde se guardarán los productos publicados
        self.usuarios = []
        self.conversaciones = []
        self.ofertas = []


#PROGRAMA PRINCIPAL

# Este bloque se ejecuta solo cuando se ejecuta este archivo
if __name__ == '__main__':

    # Creamos el marketplace
    marketplace = Marketplace()

    # # Listas donde guardaremos las personas y tarjetas
    # personas = []
    # tarjetas = []

    # Crear 10 personas con datos aleatorios
    # for i in range(10):
    #
    #     # Generamos datos aleatorios
    #     dni = generar_dni()
    #     nombre = generar_nombre()
    #     apellido = generar_apellido()
    #
    #     # Creamos el objeto Persona
    #     persona = Persona(dni, nombre, apellido)
    #
    #     # Guardamos la persona en la lista
    #     personas.append(persona)

    for i in range(10):

        dni = generar_dni()

        # Validamos el DNI antes de crear la persona
        if validar_dni(dni):
            nombre = generar_nombre()
            apellido = generar_apellido()
            persona = Persona(dni, nombre, apellido)
            marketplace.usuarios.append(persona)

        else:
            print('DNI no válido')

        # Diccionario con los datos de un producto
        datos_producto = {
            'id': '11111',
            'titulo': 'Cartera',
            'precio': 7.99,
            'estado': 'Usado',
            'stock': 1,
            'fecha_publicacion': '20-01-2025'
        }


# añadir listasssssssssss


    # MOSTRAR PERSONAS

    if len(marketplace.usuarios) == 0:
        print('No hay usuarios en el marketplace.')

    else:
        # Recorremos la lista de personas y mostramos sus datos
        for persona in marketplace.usuarios:
            print(' -', persona)


    # CREAR PRODUCTO

    if len(marketplace.usuarios) > 0:
        # Creamos manualmente un producto
        producto1 = Producto('P001', 'Cartera', 7.99, marketplace.usuarios[0],
                         'Usado', 3, '20-01-2025')
        marketplace.productos.append(producto1)

        # Comprobamos si el precio es válido
        producto1.validar_precio()

        # Comprobamos si el producto tiene stock disponible
        producto1.esta_disponible()
    else:
        print('No se puede crear productos: no hay usuarios.')


    #PUBLICAR PRODUCTO
    if len(marketplace.usuarios) > 0:
        # La primera persona publica un producto en el marketplace
        marketplace.usuarios[0].publicar_producto(datos_producto, marketplace)
    else:
        print('No se puede publicar productos: no hay usuarios.')


    # COMPRA DE PRODUCTO
    # Debe haber al menos dos usuarios
    if len(marketplace.usuarios) >= 2:
        # La segunda persona compra el producto
        marketplace.usuarios[1].comprar(producto1, 1)
        # Volvemos a comprobar el stock después de la compra
        producto1.esta_disponible()
    else:
        print('No se puede comprar: no hay suficientes usuarios.')

    # PUBLICAR PRODUCTOS ESPECIALIZADOS

    if len(marketplace.usuarios) > 0:
        # Producto ropa
        producto_ropa = ProductoRopa(
            'R001', 'Camiseta Oversize', 15.99, marketplace.usuarios[0],
            'Nuevo', 10, '15-02-2025', talla = 'M', material = 'Algodón'
        )
        marketplace.productos.append(producto_ropa)
        print('\nProducto de ropa creado:')
        print( ' -', producto_ropa)

        # Producto electrónico
        producto_elec = ProductoElectronico(
            'E001', 'Auriculares Bluetooth', 29.99, marketplace.usuarios[1],
            'Seminuevo', 5, '10-02-2025', marca = 'Sony', modelo = 'WH-CH510', garantia = 2
        )
        marketplace.productos.append(producto_elec)
        print('\nProducto electrónico creado:')
        print(' -', producto_elec)

        # Producto coche
        producto_coche = ProductoCoche(
            'C001', 'Seat Ibiza', 3500, marketplace.usuarios[2],
            'Usado', 1, '01-01-2025', matricula = '1234ABC', marca = 'Seat',
            ano = 2012, combustible = 'Gasolina', kilometros_recorridos = 145000
        )
        marketplace.productos.append(producto_coche)
        print('\nProducto coche creado:')
        print(' -', producto_coche)

        # PROBAR COMPRA DE PRODUCTOS ESPECIALIZADOS
        print('\nProbando compra de productos especializados:')

        comprador = marketplace.usuarios[3]
        comprador.importe = 5000  # Le damos dinero para probar

        comprador.comprar(producto_ropa, 1)
        comprador.comprar(producto_elec, 1)
        comprador.comprar(producto_coche, 1)

        # PROBAR CARRITP Y SOBRECARGA DE OPERADORES
        print('\nProbando carrito y sobrecarga de operadores:')

        carrito1 = Carrito(comprador)
        carrito2 = Carrito(comprador)

        carrito1.agregar_producto(producto_ropa)
        carrito1.agregar_producto(producto_elec)

        carrito2.agregar_producto(producto_coche)

        carrito_total = carrito1 + carrito2

        print(f'Carrito 1 tiene {len(carrito1)} productos.')
        print(f'Carrito 2 tiene {len(carrito2)} productos.')
        print(f'Carrito combinado tiene {len(carrito_total)} productos.')

        # PROBAR DESCUENTO PREMIUM
        tarjeta = Tarjeta('PREM123', '12/2030', descuento = 0.20)
        comprador.tarjeta_premium = tarjeta

        print('Tarjeta asignada:', tarjeta)

        comprador.importe = 1000  # Le damos dinero otra vez

        comprador.comprar(producto_elec, 1)

    else:
        print('No se pueden crear productos especializados: no hay usuarios.')
