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



if __name__ == '__main__':
    # Crear personas
    personas = []
    tarjetas = []

    for i in range(10):
        dni = generar_dni()
        nombre = generar_nombre()
        apellido = generar_apellido()

        persona = Persona(dni, nombre, apellido)

        personas.append(persona)


    # Mostrar resultados
    for persona in personas:
        print(persona)

    # Crear tarjetas premium
    cartera = Producto('11111', 'cartera', 7.99, 'Tamara', 'Usado', 1, '20-01-2025')
    cartera.validar_precio()
    cartera.esta_disponible()
