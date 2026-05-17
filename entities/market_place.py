# market_place.py

from entities.persona import Persona
from entities.producto import Producto
from entities.conversacion import Conversacion


class Marketplace:

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Persona] = []
        self.conversaciones: list[Conversacion] = []

    # USUARIOS
    def registrar_usuario(self, persona: Persona) -> None:
        if not isinstance(persona, Persona):
            raise TypeError('Solo se pueden registrar objetos Persona.')

        if persona in self.usuarios:
            raise ValueError('El usuario ya está registrado.')

        self.usuarios.append(persona)

    def listar_usuarios(self) -> list[Persona]:
        return self.usuarios[:]


    # PRODUCTOS

    def registrar_producto(self, producto: Producto) -> None:
        if not isinstance(producto, Producto):
            raise TypeError('Solo se pueden registrar objetos Producto.')

        self.productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        return self.productos[:]

    def buscar_producto(self, id_producto: str) -> Producto:
        for p in self.productos:
            if p.id == id_producto:
                return p
        raise ValueError('Producto no encontrado.')

    def eliminar_producto(self, producto: Producto) -> None:
        if producto not in self.productos:
            raise ValueError('El producto no está en el marketplace.')
        self.productos.remove(producto)


    # BÚSQUEDAS

    def buscar_por_titulo(self, texto: str) -> list[Producto]:
        return [p for p in self.productos if texto.lower() in p.titulo.lower()]

    def buscar_por_tipo(self, tipo: type) -> list[Producto]:
        return [p for p in self.productos if isinstance(p, tipo)]


    # CONVERSACIONES

    def iniciar_conversacion(self, usuario1: Persona, usuario2: Persona) -> Conversacion:
        conv = Conversacion(usuario1, usuario2)
        self.conversaciones.append(conv)
        return conv

    def solicitar_tarjeta_premium(self, usuario: Persona) -> None:
        if usuario.compras_realizadas < 3:
            raise ValueError('El usuario no cumple los requisitos para obtener tarjeta premium.')

        usuario.tarjeta_premium = TarjetaPremium(
            codigo=generar_codigo_unico(),
            fecha_caducidad='12/2030',
            descuento=0.20
        )

    def buscar_usuario_por_dni(self, dni: str):
        for u in self.usuarios:
            if u.dni == dni:
                return u
        return None
