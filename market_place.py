# market_place.py
from persona import Persona
from tarjeta_premium import Tarjeta
from producto import Producto
import random

# Funciones
def generar_dni():
    letra_aleatoria = chr(random.randint(65, 90))
    numeros = random.randint(11111111,99999999)
    dni = str(numeros) + letra_aleatoria

    return dni

def generar_nombre():
    nombres = [
        'Carlos', 'Lucía', 'María', 'Pedro', 'Ana',
        'Javier', 'Marta', 'Sofía', 'Diego', 'Elena',
        'Raúl', 'Nohelia', 'Iván', 'Laura', 'Miguel'
    ]

    return random.choice(nombres)

def generar_apellido():
    apellidos = [
        'García', 'López', 'Martínez', 'Sánchez',
        'Pérez', 'Gómez', 'Ruiz', 'Fernández',
        'Torres', 'Díaz', 'Morales', 'Romero'
    ]
    return random.choice(apellidos)

class Marketplace:
    def __init__(self):
        self.productos = []


if __name__ == '__main__':
    marketplace = Marketplace()
    # Crear personas
    personas = []
    tarjetas = []

    for i in range(10):
        dni = generar_dni()
        nombre = generar_nombre()
        apellido = generar_apellido()

        persona = Persona(dni, nombre, apellido)

        personas.append(persona)

        datos_producto = {
            "id": "11111",
            "titulo": "Cartera",
            "precio": 7.99,
            "estado": "Usado",
            "stock": 1,
            "fecha_publicacion": "20-01-2025"
        }

# añadir listasssssssssss


    # Mostrar resultados
    for persona in personas:
        print(persona)

    # Crear tarjetas premium
    cartera = Producto('11111', 'monedero', 7.99, 'Tamara', 'Usado', 1, '20-01-2025')
    cartera.validar_precio()
    cartera.esta_disponible()

    personas[0].publicar_producto(datos_producto, marketplace)
    personas[1].comprar(cartera, 1)
    cartera.esta_disponible()



