# persona.py

class Persona:
    def __init__(self, dni, nombre, apellido, email, tarjeta_premium = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta_premium = tarjeta_premium

    def __str__(self):
        cadena = f'Nombre y Apellido: {self.nombre} {self.apellido} -DNI: {self.dni}'

        if self.tarjeta_premium:
            cadena += f' -Tarjeta: {self.tarjeta_premium}'

        return cadena
