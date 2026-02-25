# persona.py
from producto import Producto

class Persona:
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
       # self.email = email
        self.tarjeta_premium = tarjeta_premium

    def __str__(self):
        cadena = f'Nombre y Apellido: {self.nombre} {self.apellido} -DNI: {self.dni}'

        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premium}'

        return cadena

    def publicar_producto(self, datos_producto, marketplace):
        producto = Producto.desde_diccionario(datos_producto, self)
        marketplace.productos.append(producto)
        print(f'{self.nombre} {self.apellido} publicó el producto: {producto.titulo} a {producto.precio}€, el día {producto.fecha_publicacion}')


    def comprar(self, producto, cantidad):
        if not producto.esta_disponible():
            print('Producto no disponible')
            return
        #
        # if self.importe < producto.precio:
        #     print('Importe insuficiente')
        #     return True
        producto.reducir_stock(cantidad)
        print(f' {self.nombre} compró {producto.titulo}')

    def enviar_mensaje(self, conversacion, texto):
        conversacion.agregar_mensaje(self, texto)
#terminar