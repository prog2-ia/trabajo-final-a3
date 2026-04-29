# persona.py

# Importamos la clase Producto desde el archivo producto.py
from entities.producto import Producto
from entities.conversacion import Conversacion
from entities.tarjeta_premium import TarjetaPremium

# Definición de la clase Persona
class Persona:

    # Constructor de la clase.
    # Se ejecuta cuando se crea una nueva persona.
    def __init__(self, dni: str, nombre: str, apellido: str, tarjeta_premium: 'TarjetaPremium' = None, importe: float = 0.0) -> None:
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

        # Se crea un objeto Producto a partir de un diccionario de datos
        # y se asocia a esta persona como vendedor
        producto = Producto.desde_diccionario(datos_producto, self)

        # Se añade el producto a la lista de productos del marketplace
        marketplace.productos.append(producto)

        return producto
        # Mensaje informativo
        # print(f'{self.nombre} {self.apellido} publicó el producto: {producto.titulo} a {producto.precio}€, el día {producto.fecha_publicacion}')


    # Metodo para comprar un producto
    def comprar(self, producto: Producto, cantidad: int) -> dict:

        # Comprobamos si el producto está disponible
        if not producto.esta_disponible():
            return {'ok': False, 'motivo': 'Producto no disponible'}

        # Restar dinero al comprador
        precio_total = producto.precio * cantidad

        # Aplicamos descuento si tiene tarjeta premium
        if self.tarjeta_premium:
            precio_total = self.tarjeta_premium.aplicar_descuento(precio_total)

        if self.importe < precio_total:
            return {'ok': False, 'motivo': 'Importe insuficiente'}

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

    def meter_saldo(self, cantidad: float) -> bool:
        if cantidad <= 0:
            return False
        self.importe += cantidad
        return True
