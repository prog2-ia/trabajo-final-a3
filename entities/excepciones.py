#excepciones.py

class StockError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class UsuarioNoAutorizadoError(Exception):
    pass

class PrecioInvalidoError(Exception):
    pass
