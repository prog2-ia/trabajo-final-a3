# persona.py

# Importamos la clase Producto desde el archivo producto.py
from producto import Producto


# Definición de la clase Persona
class Persona:

    # Constructor de la clase.
    # Se ejecuta cuando se crea una nueva persona.
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None, importe = 0):
        self.dni = dni                # DNI de la persona
        self.nombre = nombre          # Nombre de la persona
        self.apellido = apellido      # Apellido de la persona
        # self.email = email          # Email
        self.tarjeta_premium = tarjeta_premium  # Tarjeta premium opcional
        self.importe = importe        # Importe


    # Metodo especial que define cómo se muestra el objeto al imprimirlo
    def __str__(self):

        # Creamos una cadena con los datos básicos
        cadena = f'Nombre y Apellido: {self.nombre} {self.apellido} -DNI: {self.dni}'

        # Si la persona tiene tarjeta premium, se añade a la cadena
        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premium}'

        # Devolvemos la cadena final
        return cadena


    # Metodo para que una persona publique un producto en el marketplace
    def publicar_producto(self, datos_producto, marketplace):

        # Se crea un objeto Producto a partir de un diccionario de datos
        # y se asocia a esta persona como vendedor
        producto = Producto.desde_diccionario(datos_producto, self)

        # Se añade el producto a la lista de productos del marketplace
        marketplace.productos.append(producto)

        # Mensaje informativo
        print(f'{self.nombre} {self.apellido} publicó el producto: {producto.titulo} a {producto.precio}€, el día {producto.fecha_publicacion}')


    # Metodo para comprar un producto
    def comprar(self, producto, cantidad):

        # Comprobamos si el producto está disponible
        if not producto.esta_disponible():
            print('Producto no disponible')
            return False

        # Comprobación de dinero disponible
        # if self.importe < producto.precio:
        #     print('Importe insuficiente')
        #     return True

        # Restar dinero al comprador
        precio_total = producto.precio * cantidad

        # Aplicamos descuento si tiene tarjeta premium
        if self.tarjeta_premium:
            precio_total = self.tarjeta_premium.aplicar_descuento(precio_total)

        if self.importe < precio_total:
            print('Importe insuficiente')
            return False

        self.importe -= precio_total

        # Reducimos el stock del producto según la cantidad comprada
        producto.reducir_stock(cantidad)

        # Mensaje de confirmación de compra
        print(f' {self.nombre} compró {producto.titulo}')


    # Metodo para enviar un mensaje dentro de una conversación
    def enviar_mensaje(self, conversacion, texto):

        # Se añade el mensaje a la conversación indicando quién lo envía
        conversacion.agregar_mensaje(self, texto)

