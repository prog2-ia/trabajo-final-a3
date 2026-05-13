# menu.py

class MenuCLI:

    def __init__(self, marketplace_service, usuarios_service, productos_service, conversaciones_service):
        self.marketplace_service = marketplace_service
        self.usuarios_service = usuarios_service
        self.productos_service = productos_service
        self.conversaciones_service = conversaciones_service

    def mostrar_menu(self):
        print('\n===== MARKETPLACE — MENÚ PRINCIPAL =====')
        print('1. Registrar usuario')
        print('2. Listar usuarios')
        print('3. Publicar producto')
        print('4. Listar productos')
        print('5. Comprar producto')
        print('6. Buscar producto por título')
        print('7. Buscar producto por tipo')
        print('8. Solicitar tarjeta premium')
        print('9. Iniciar conversación')
        print('10. Enviar mensaje')
        print('11. Ver historial de conversación')
        print('0. Salir')

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input('\nSelecciona una opción: ')

            try:
                if opcion == '1':
                    self.usuarios_service.registrar_usuario_cli()

                elif opcion == '2':
                    self.usuarios_service.listar_usuarios_cli()

                elif opcion == '3':
                    self.productos_service.publicar_producto_cli()

                elif opcion == '4':
                    self.productos_service.listar_productos_cli()

                elif opcion == '5':
                    self.productos_service.comprar_producto_cli()

                elif opcion == '6':
                    self.productos_service.buscar_por_titulo_cli()

                elif opcion == '7':
                    self.productos_service.buscar_por_tipo_cli()

                elif opcion == '8':
                    self.usuarios_service.solicitar_tarjeta_premium_cli()

                elif opcion == '9':
                    self.conversaciones_service.iniciar_conversacion_cli()

                elif opcion == '10':
                    self.conversaciones_service.enviar_mensaje_cli()

                elif opcion == '11':
                    self.conversaciones_service.ver_historial_cli()

                elif opcion == '0':
                    print('Saliendo del programa...')
                    break

                else:
                    print('Opción no válida.')

            except Exception as e:
                print('Error:', e)

