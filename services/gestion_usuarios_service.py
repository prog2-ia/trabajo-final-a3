# services/gestion_usuarios_service.py

from entities.persona import Persona
from entities.tarjeta_premium import TarjetaPremium


class GestionUsuariosService:

    def __init__(self, marketplace):
        self.marketplace = marketplace

    # -----------------------------
    # MÉTODOS DE LÓGICA
    # -----------------------------
    def registrar_usuario(self, dni, nombre, apellido):
        usuario = Persona(dni, nombre, apellido)
        self.marketplace.registrar_usuario(usuario)
        return usuario

    def listar_usuarios(self):
        return self.marketplace.listar_usuarios()

    def solicitar_tarjeta_premium(self, usuario):
        if usuario.compras_realizadas < 3:
            raise ValueError('El usuario no cumple los requisitos: necesita 3 compras distintas.')

        usuario.tarjeta_premium = TarjetaPremium(
            codigo=f'PREM-{usuario.dni}',
            fecha_caducidad='12/2030',
            descuento=0.20
        )
        return usuario.tarjeta_premium

    # -----------------------------
    # MÉTODOS CLI
    # -----------------------------
    def registrar_usuario_cli(self):
        print('\n--- Registrar usuario ---')
        dni = input('DNI: ')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')

        try:
            usuario = self.registrar_usuario(dni, nombre, apellido)
            print('Usuario registrado:', usuario)
        except Exception as e:
            print('Error:', e)

    def listar_usuarios_cli(self):
        print('\n--- Lista de usuarios ---')
        usuarios = self.listar_usuarios()

        if not usuarios:
            print('No hay usuarios registrados.')
            return

        for u in usuarios:
            print(' -', u)

    def solicitar_tarjeta_premium_cli(self):
        print('\n--- Solicitar tarjeta premium ---')
        dni = input('DNI del usuario: ')

        usuario = self.marketplace.buscar_usuario_por_dni(dni)
        if usuario is None:
            print('Usuario no encontrado.')
            return

        try:
            tarjeta = self.solicitar_tarjeta_premium(usuario)
            print('Tarjeta premium asignada:', tarjeta)
        except Exception as e:
            print('Error:', e)



def buscar_por_titulo(marketplace):
    texto = input('\nTexto a buscar: ')
    resultados = marketplace.buscar_por_titulo(texto)

    if not resultados:
        print('No se encontraron productos.')
        return

    print('\nResultados:')
    for p in resultados:
        print(' -', p)


def buscar_por_tipo(marketplace):
    print('\n1. Ropa\n2. Electrónico\n3. Coche')
    tipo = input('Selecciona tipo: ')

    if tipo == '1':
        resultados = marketplace.buscar_por_tipo(ProductoRopa)
    elif tipo == '2':
        resultados = marketplace.buscar_por_tipo(ProductoElectronico)
    elif tipo == '3':
        resultados = marketplace.buscar_por_tipo(ProductoCoche)
    else:
        print('Tipo no válido.')
        return

    if not resultados:
        print('No se encontraron productos.')
        return

    print('\nResultados:')
    for p in resultados:
        print(' -', p)


def solicitar_tarjeta_premium(marketplace):
    print('\n--- Solicitar tarjeta premium ---')

    dni = input('DNI del usuario: ')
    usuario = next((u for u in marketplace.usuarios if u.dni == dni), None)

    if usuario is None:
        print('Usuario no encontrado.')
        return

    if usuario.compras_realizadas < 3:
        print('No puedes obtener tarjeta premium. Necesitas 3 compras distintas.')
        return

    usuario.tarjeta_premium = TarjetaPremium('PREM-' + usuario.dni, '12/2030', 0.20)
    print('Tarjeta premium asignada:', usuario.tarjeta_premium)


# def menu():
#     marketplace = Marketplace()
#
#     while True:
#         print('\n===== MARKETPLACE AVANZADO =====')
#         print('1. Registrar usuario')
#         print('2. Listar usuarios')
#         print('3. Publicar producto')
#         print('4. Listar productos')
#         print('5. Comprar producto')
#         print('6. Buscar producto por título')
#         print('7. Buscar producto por tipo')
#         print('8. Solicitar tarjeta premium')
#         print('0. Salir')
#
#         opcion = pedir_opcion()
#
#         if opcion == 1:
#             registrar_usuario(marketplace)
#         elif opcion == 2:
#             listar_usuarios(marketplace)
#         elif opcion == 3:
#             publicar_producto(marketplace)
#         elif opcion == 4:
#             listar_productos(marketplace)
#         elif opcion == 5:
#             comprar_producto(marketplace)
#         elif opcion == 6:
#             buscar_por_titulo(marketplace)
#         elif opcion == 7:
#             buscar_por_tipo(marketplace)
#         elif opcion == 8:
#             solicitar_tarjeta_premium(marketplace)
#         elif opcion == 0:
#             print('Saliendo del programa...')
#             break
#         else:
#             print('Opción no válida.')
#
#
# if __name__ == '__main__':
#     menu()
