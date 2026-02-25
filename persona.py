# persona.py
from producto import Producto


class Persona:
    def __init__(self, dni, nombre, apellido, email, tarjeta_premium = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta_premium = tarjeta_premium

    def __str__(self):
        cadena = f'Nombre y Apellido: {self.nombre} {self.apellido} -DNI: {self.dni}'

        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premium}'

        return cadena

    def publicar_producto(self, producto, marketplace):
        marketplace.producto.append(Producto())
        print(f'{self.nombre} publicó el producto: {producto.titulo}')


    def comprar(self, producto):
        if not producto.esta_disponible():
            print('Producto no disponible')
            return True

        if self.importe < producto.precio:
            print('Importe insuficiente')
            return True
        producto.reducir_stock()
        print(f' {self.nombre} compró {producto.titulo}')

    def enviar_mensaje(self, conversacion, texto):
            conversacion.agregar_mensaje(self, texto)
#terminar