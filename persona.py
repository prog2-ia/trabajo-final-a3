# persona.py

class Persona:
    def __init__(self, dni, nombre, apellido, tarjeta_premium = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.tarjeta_premium = tarjeta_premium

    def __str__(self):
        cadena = f'Persona {self.nombre} {self.apellido} -DNI: {self.dni}'

        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premiu}'

        return cadena
