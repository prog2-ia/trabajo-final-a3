#gestion_conversaciones_service.py

# services/gestion_conversaciones_service.py

class GestionConversacionesService:

    def __init__(self, marketplace):
        self.marketplace = marketplace

    # -----------------------------
    # LÓGICA
    # -----------------------------
    def iniciar_conversacion(self, usuario1, usuario2):
        return self.marketplace.iniciar_conversacion(usuario1, usuario2)

    def enviar_mensaje(self, conversacion, autor, texto):
        conversacion.agregar_mensaje(autor, texto)

    def ver_historial(self, conversacion):
        return conversacion.obtener_historial()

    # -----------------------------
    # CLI
    # -----------------------------
    def iniciar_conversacion_cli(self):
        print('\n--- Iniciar conversación ---')

        dni1 = input('DNI del usuario 1: ')
        dni2 = input('DNI del usuario 2: ')

        u1 = self.marketplace.buscar_usuario_por_dni(dni1)
        u2 = self.marketplace.buscar_usuario_por_dni(dni2)

        if not u1 or not u2:
            print('Uno o ambos usuarios no existen.')
            return

        try:
            conv = self.iniciar_conversacion(u1, u2)
            print('Conversación iniciada.')
        except Exception as e:
            print('Error:', e)

    def enviar_mensaje_cli(self):
        print('\n--- Enviar mensaje ---')

        dni = input('DNI del autor: ')
        autor = self.marketplace.buscar_usuario_por_dni(dni)

        if autor is None:
            print('Usuario no encontrado.')
            return

        idx = int(input('Índice de conversación: '))
        try:
            conversacion = self.marketplace.conversaciones[idx]
        except:
            print('Conversación no encontrada.')
            return

        texto = input('Mensaje: ')

        try:
            self.enviar_mensaje(conversacion, autor, texto)
            print('Mensaje enviado.')
        except Exception as e:
            print('Error:', e)

    def ver_historial_cli(self):
        print('\n--- Ver historial ---')

        idx = int(input('Índice de conversación: '))
        try:
            conversacion = self.marketplace.conversaciones[idx]
        except:
            print('Conversación no encontrada.')
            return

        historial = self.ver_historial(conversacion)

        if not historial:
            print('No hay mensajes.')
            return

        for m in historial:
            print(' -', m)