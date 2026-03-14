# market_place.py

# Importamos las clases necesarias del proyecto
from persona import Persona
from tarjeta_premium import Tarjeta
from producto import Producto
import random


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


#PROGRAMA PRINCIPAL

# Este bloque se ejecuta solo cuando se ejecuta este archivo
if __name__ == '__main__':

    # Creamos el marketplace
    marketplace = Marketplace()

    # Listas donde guardaremos las personas y tarjetas
    personas = []
    tarjetas = []

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

            personas.append(persona)

        else:
            print("DNI no válido")

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

    # Recorremos la lista de personas y mostramos sus datos
    for persona in personas:
        print(persona)


    # CREAR PRODUCTO

    # Creamos manualmente un producto
    cartera = Producto('11111', 'monedero', 7.99, 'Ruperta', 'Usado', 1, '20-01-2025')

    # Comprobamos si el precio es válido
    cartera.validar_precio()

    # Comprobamos si el producto tiene stock disponible
    cartera.esta_disponible()


    #PUBLICAR PRODUCTO

    # La primera persona publica un producto en el marketplace
    personas[0].publicar_producto(datos_producto, marketplace)


    # COMPRA DE PRODUCTO

    # La segunda persona compra el producto
    personas[1].comprar(cartera, 1)


    # Volvemos a comprobar el stock después de la compra
    cartera.esta_disponible()



