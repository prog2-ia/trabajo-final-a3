# carrito.py

class Carrito:
    def __init__(self, comprador, lista_productos):
        self.comprador = comprador
        self.lista_productos = lista_productos


    def agregar_productos(self):
        self.lista_productos.add()

    def eliminar_productos(self):
        self.lista_productos.clear()

  #  def calcular_total(self):
      #  total = 0
        #for producto in self.lista_productos:
           # total += producto.valor
           # return total

