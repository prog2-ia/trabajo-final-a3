# publicacion.py

from abc import ABC, abstractmethod

# Clase abstracta Publicacion
class Publicacion(ABC):

    def __init__(self):
        # Constructor para futuras ampliaciones
        pass

    # Metodo abstracto que debe mostrar la info de la publicacion
    # Cada clase hija decidira como mostrar los datos
    @abstractmethod
    def mostrar_info(self):
        pass

    # Metodo abstracto que debe calcular el precio final
    @abstractmethod
    def calcular_precio_final(self):
        pass

