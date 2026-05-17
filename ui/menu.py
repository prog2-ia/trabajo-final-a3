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
        print('12. Guardar datos en ficheros de texto')
        print('13. Guardar marketplace en pickle')
        print('14. Cargar marketplace desde pickle')
        print('15. Listar ficheros en data/')
        print('16. Leer cabecera de fichero binario')
        print('17. Crear copia de seguridad de data/')
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

                elif opcion == '12':
                    self.marketplace_service.guardar_datos_texto()
                    print('Datos guardados en ficheros de texto.')

                elif opcion == '13':
                    self.marketplace_service.guardar_marketplace_pickle()
                    print('Marketplace guardado en pickle.')

                elif opcion == '14':
                    try:
                        self.marketplace_service.cargar_marketplace_pickle()
                        print('Marketplace cargado desde pickle.')
                    except Exception as e:
                        print('Error:', e)

                elif opcion == '15':
                    entries = self.marketplace_service.listar_data()
                    if not entries:
                        print('No hay ficheros en data/.')
                    else:
                        print('\nFicheros en data/:')
                        for e in entries:
                            print(' -', e)

                elif opcion == '16':
                    ruta = input('Ruta del fichero binario: ')
                    try:
                        cab = self.marketplace_service.leer_cabecera_binaria(ruta)
                        print('Cabecera (bytes):', cab)
                    except Exception as e:
                        print('Error:', e)

                elif opcion == '17':
                    try:
                        self.marketplace_service.crear_backup()
                        print('Copia de seguridad creada en data/backup/')
                    except Exception as e:
                        print('Error:', e)

                elif opcion == '0':
                    print('Saliendo del programa...')
                    break

                else:
                    print('Opción no válida.')

            except Exception as e:
                print('Error:', e)

