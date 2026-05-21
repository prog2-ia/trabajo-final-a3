# market_place.py

from entities.persona import Persona
from entities.producto import Producto
from entities.conversacion import Conversacion
from entities.tarjeta_premium import TarjetaPremium
import random


class Marketplace:

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Persona] = []
        self.conversaciones: list[Conversacion] = []

    # USUARIOS
    def registrar_usuario(self, persona: Persona) -> None:
        if not isinstance(persona, Persona):
            raise TypeError('Solo se pueden registrar objetos Persona.')

        for usuario in self.usuarios:

            if usuario.dni == persona.dni:
                raise ValueError('Ya existe un usuario con ese DNI.')

        self.usuarios.append(persona)

    def listar_usuarios(self) -> list[Persona]:
        return self.usuarios[:]


    # PRODUCTOS

    def registrar_producto(self, producto: Producto) -> None:
        if not isinstance(producto, Producto):
            raise TypeError('Solo se pueden registrar objetos Producto.')

        for p in self.productos:
            if p.id == producto.id:
                raise ValueError('Ya existe un producto con ese ID.')

        self.productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        return [p for p in self.productos if not p.eliminado]

    def buscar_producto(self, id_producto: str) -> Producto:
        for p in self.productos:
            if p.id == id_producto and not p.eliminado:
                return p
        raise ValueError('Producto no encontrado.')

    def eliminar_producto(self, producto: Producto) -> None:
        if producto not in self.productos:
            raise ValueError('El producto no está en el marketplace.')

        producto.eliminado = True


    # BÚSQUEDAS
    def buscar_por_titulo(self, texto: str) -> list[Producto]:
        return [p for p in self.productos if (texto.lower() in p.titulo.lower() and not p.eliminado)]

    def buscar_por_tipo(self, tipo: type) -> list[Producto]:
        return [p for p in self.productos if (isinstance(p, tipo) and not p.eliminado)]


    # CONVERSACIONES
    def iniciar_conversacion(self, usuario1: Persona, usuario2: Persona) -> Conversacion:
        for c in self.conversaciones:
            mismos = (
                    (c.usuarios[0] == usuario1 and c.usuarios[1] == usuario2)
                    or
                    (c.usuarios[0] == usuario2 and c.usuarios[1] == usuario1)
            )

            if mismos:
                return c

        conv = Conversacion(usuario1, usuario2)
        self.conversaciones.append(conv)
        return conv

    def solicitar_tarjeta_premium(self, usuario: Persona) -> None:
        if usuario.compras_realizadas < 3:
            raise ValueError('El usuario no cumple los requisitos para obtener tarjeta premium.')
        if usuario.tarjeta_premium:
            raise ValueError('El usuario ya tiene tarjeta premium.')

        codigo = f'PREM-{random.randint(1000, 9999)}'
        usuario.tarjeta_premium = TarjetaPremium(
            codigo=codigo,
            fecha_caducidad='12/2030',
            descuento=0.20
        )

    def buscar_usuario_por_dni(self, dni: str):
        for u in self.usuarios:
            if u.dni == dni:
                return u
        return None
