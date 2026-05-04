# persona.py

# Importamos la clase Producto desde el archivo producto.py
from entities.producto import Producto
from entities.conversacion import Conversacion
from entities.tarjeta_premium import TarjetaPremium
from entities.excepciones import SaldoInsuficienteError

# Definición de la clase Persona
class Persona:

    # Constructor de la clase.
    # Se ejecuta cuando se crea una nueva persona.
    def __init__(self, dni: str, nombre: str, apellido: str, tarjeta_premium: 'TarjetaPremium' = None, importe: float = 0.0) -> None:

        if not dni or dni.strip() == '':
            raise ValueError('El DNI no puede estar vacío.')

        if not nombre or nombre.strip() == '':
            raise ValueError('El nombre no puede estar vacío.')

        if not apellido or apellido.strip() == '':
            raise ValueError('El apellido no puede estar vacío.')

        if importe < 0:
            raise ValueError('El importe no puede ser negativo.')

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        # self.email = email
        self.tarjeta_premium = tarjeta_premium
        self.importe = importe


    # Metodo especial que define cómo se muestra el objeto al imprimirlo
    def __str__(self) -> str:

        # Creamos una cadena con los datos básicos
        cadena = f'{self.nombre} {self.apellido} -DNI: {self.dni}'

        # Si la persona tiene tarjeta premium, se añade a la cadena
        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premium}'

        return cadena


    # Metodo para que una persona publique un producto en el marketplace
    def publicar_producto(self, datos_producto: dict, marketplace: object) -> Producto:

        if not isinstance(datos_producto, dict):
            raise TypeError('Los datos de producto deben estar en un diccionario.')

        if not hasattr(marketplace, 'productos'):
            raise AttributeError('El marketplace no es válido.')

        # Se crea un objeto Producto a partir de un diccionario de datos
        # y se asocia a esta persona como vendedor
        producto = Producto.desde_diccionario(datos_producto, self)

        # Se añade el producto a la lista de productos del marketplace
        marketplace.productos.append(producto)

        return producto

    # Metodo para comprar un producto
    def comprar(self, producto: Producto, cantidad: int) -> dict:

        if not isinstance(producto, Producto):
            raise TypeError('Debes proporcionar un objeto Producto.')

        if cantidad <= 0:
            raise ValueError('El cantidad no puede ser negativa.')

        if not producto.esta_disponible():
            raise Exception('Producto no disponible.')

        # Restar dinero al comprador
        precio_total = producto.precio * cantidad

        # Aplicamos descuento si tiene tarjeta premium
        if self.tarjeta_premium:
            precio_total = self.tarjeta_premium.aplicar_descuento(precio_total)

        if self.importe < precio_total:
            raise SaldoInsuficienteError('No tienes saldo suficiente.')

        # Actualizar saldo y stock
        self.importe -= precio_total
        producto.reducir_stock(cantidad)

        return {
            'ok': True,
            'producto': producto.titulo,
            'cantidad': cantidad,
            'precio_pagado': precio_total
        }


    # Metodo para enviar un mensaje dentro de una conversación
    def enviar_mensaje(self, conversacion: Conversacion, texto: str) -> bool:

        # Se añade el mensaje a la conversación indicando quién lo envía
        conversacion.agregar_mensaje(self, texto)
        return True

    def meter_saldo(self, cantidad: float) -> bool:
        if cantidad <= 0:
            raise ValueError('El cantidad no puede ser negativa.')
        self.importe += cantidad
        return True

    def ver_saldo(self) -> float:
        return self.importe

    def tiene_tarjeta_premium(self) -> bool:
        return self.tarjeta_premium is not None



