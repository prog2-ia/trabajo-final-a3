# main.py

from persona import Persona
from tarjeta_premium import Tarjeta

if __name__ == '__main__':
    # Crear personas
    persona1 = Persona('72019838Y', 'Carolina', 'Marzo')
    persona2 = Persona('13033927S', 'Aurelio', 'Roldán')
    persona3 = Persona('33901875T', 'Elena', 'Barea')
    persona4 = Persona('78901765M', 'Ainoha', 'Bogarea')
    persona5 = Persona('78201823O', 'Nohelia', 'Montoya')
    persona6 = Persona('19029187J', 'Ronny', 'Belger')
    persona7 = Persona('91802738P', 'Benny', 'Polay')

    # Crear tarjetas premium
    tarjeta1 = Tarjeta()
    tarjeta2 = Tarjeta