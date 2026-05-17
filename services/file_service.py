# services/file_service.py

import os
import shutil
import pickle

DATA_DIR = 'data'
USUARIOS_FILE = os.path.join(DATA_DIR, 'usuarios.txt')
PRODUCTOS_FILE = os.path.join(DATA_DIR, 'productos.txt')
BIN_TEST_FILE = os.path.join(DATA_DIR, 'test.bin')
PICKLE_FILE = os.path.join(DATA_DIR, 'marketplace.pickle')
BACKUP_DIR = os.path.join(DATA_DIR, 'backup')


class FileService:

    def __init__(self) -> None:
        self._asegurar_estructura()

    def _asegurar_estructura(self) -> None:
        os.makedirs(DATA_DIR, exist_ok=True)
        os.makedirs(BACKUP_DIR, exist_ok=True)

    # ---------- TEXTO ----------

    def guardar_usuarios_texto(self, usuarios: list) -> None:
        with open(USUARIOS_FILE, 'w', encoding='utf-8') as f:
            for u in usuarios:
                linea = f'{u.dni};{u.nombre};{u.apellido};{u.importe}\n'
                f.write(linea)

    def guardar_productos_texto(self, productos: list) -> None:
        with open(PRODUCTOS_FILE, 'w', encoding='utf-8') as f:
            for p in productos:
                linea = f'{p.id};{p.titulo};{p.precio};{p.stock};{p.fecha_publicacion}\n'
                f.write(linea)

    def leer_fichero_texto(self, ruta: str) -> str:
        if not os.path.exists(ruta):
            raise FileNotFoundError('El fichero no existe.')
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()

    # ---------- BINARIO ----------

    def escribir_binario_demo(self) -> None:
        with open(BIN_TEST_FILE, 'wb') as f:
            f.write(b'\x89BINDEMO\r\n\x1a\n')

    def leer_cabecera_binaria(self, ruta: str, n_bytes: int = 8) -> bytes:
        with open(ruta, 'rb') as f:
            return f.read(n_bytes)

    # ---------- PICKLE ----------

    def guardar_marketplace_pickle(self, marketplace) -> None:
        with open(PICKLE_FILE, 'wb') as f:
            pickle.dump(marketplace, f)

    def cargar_marketplace_pickle(self):
        if not os.path.exists(PICKLE_FILE):
            raise FileNotFoundError('No existe el fichero pickle del marketplace.')
        with open(PICKLE_FILE, 'rb') as f:
            return pickle.load(f)

    # ---------- DIRECTORIOS / FICHEROS ----------

    def listar_data(self) -> list[str]:
        if not os.path.exists(DATA_DIR):
            return []
        return os.listdir(DATA_DIR)

    def crear_backup(self) -> None:
        if os.path.exists(BACKUP_DIR):
            shutil.rmtree(BACKUP_DIR)
        os.makedirs(BACKUP_DIR, exist_ok=True)
        for entry in os.scandir(DATA_DIR):
            if entry.is_file():
                shutil.copy(entry.path, BACKUP_DIR)

    def existe_fichero(self, ruta: str) -> bool:
        import os
        return os.path.exists(ruta)
