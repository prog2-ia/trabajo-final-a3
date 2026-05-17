from services.file_service import FileService


class GestionMarketplaceService:

    def __init__(self, marketplace):
        self.marketplace = marketplace
        self.file_service = FileService()

    def obtener_marketplace(self):
        return self.marketplace

    # --------- TEXTO ---------

    def guardar_datos_texto(self):
        self.file_service.guardar_usuarios_texto(self.marketplace.usuarios)
        self.file_service.guardar_productos_texto(self.marketplace.productos)

    def mostrar_fichero_texto(self, ruta: str) -> str:
        return self.file_service.leer_fichero_texto(ruta)

    # --------- PICKLE ---------

    def guardar_marketplace_pickle(self):
        self.file_service.guardar_marketplace_pickle(self.marketplace)

    def cargar_marketplace_pickle(self):
        nuevo = self.file_service.cargar_marketplace_pickle()
        self.marketplace.usuarios = nuevo.usuarios
        self.marketplace.productos = nuevo.productos
        self.marketplace.conversaciones = nuevo.conversaciones

    # --------- BINARIO ---------

    def demo_binario(self):
        self.file_service.escribir_binario_demo()
        return self.file_service.leer_cabecera_binaria(self.file_service.BIN_TEST_FILE) \
            if hasattr(self.file_service, 'BIN_TEST_FILE') else None

    def leer_cabecera_binaria(self, ruta: str, n_bytes: int = 8) -> bytes:
        return self.file_service.leer_cabecera_binaria(ruta, n_bytes)

    # --------- DIRECTORIOS / BACKUP ---------

    def listar_data(self) -> list[str]:
        return self.file_service.listar_data()

    def crear_backup(self):
        self.file_service.crear_backup()


