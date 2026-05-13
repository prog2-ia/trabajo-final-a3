# conversacion.py

# Importamos la clase Mensaje desde el archivo mensaje.py.
from entities.mensaje import Mensaje
from entities.excepciones import UsuarioNoAutorizadoError

# Clase Conversacion
class Conversacion:
    # Constructor de la clase
    # Se ejecuta cuando se crea una conversacion
    def __init__(self, usuario1: object, usuario2: object) -> None:

        if usuario1 is None or usuario2 is None:
            raise ValueError('Debe haber dos usuarios para mantener una conversación.')

        if usuario1 == usuario2:
            raise ValueError('No te puedes enviar un mensaje a ti mismo.')

        if not hasattr(usuario1, 'nombre') or not hasattr(usuario2, 'nombre'):
            raise TypeError('Los usuarios deben ser objetos válidos con atributo nombre.')

        self.usuarios = (usuario1, usuario2)
        self.mensajes: list[Mensaje] = []

    # Metodo para añadir mensajes
    def agregar_mensaje(self, autor: object, texto: str) -> bool:

        if autor not in self.usuarios:
            raise UsuarioNoAutorizadoError('El autor no pertenece a esta conversación.')

        if hasattr(autor, 'nombre'):
            raise TypeError('El autor debe ser un objeto válido con atributo nombre.')

        if not texto or texto.strip() == '':
            raise ValueError('El texto no puede estar vacío.')

        mensaje = Mensaje(autor, texto)
        self.mensajes.append(mensaje)
        return True

        # Devolver historial de mensajes
    def obtener_historial(self) -> list[Mensaje]:
        return self.mensajes[:]

    def ultimo_mensaje(self) -> Mensaje | None:
        if self.mensajes:
            return self.mensajes[-1]
        else:
            return None

    def cantidad_mensajes(self) -> int:
        return len(self.mensajes)

    # Representación opcional de la conversación
    def __str__(self) -> str:
        return f'Conversación entre {self.usuarios[0].nombre} y {self.usuarios[1].nombre}'

