# main.py

from entities.marketplace import Marketplace
from services.gestion_marketplace_service import GestionMarketplaceService
from services.gestion_usuarios_service import GestionUsuariosService
from services.gestion_productos_service import GestionProductosService
from services.gestion_conversaciones_service import GestionConversacionesService
from services.seed_data_service import SeedDataService
from ui.menu import MenuCLI


def main():
    marketplace = Marketplace()

    marketplace_service = GestionMarketplaceService(marketplace)
    usuarios_service = GestionUsuariosService(marketplace)
    productos_service = GestionProductosService(marketplace)
    conversaciones_service = GestionConversacionesService(marketplace)

    seed_service = SeedDataService(productos_service, usuarios_service)
    seed_service.cargar_datos_demo()

    menu = MenuCLI(marketplace_service, usuarios_service, productos_service, conversaciones_service)
    menu.ejecutar()


if __name__ == '__main__':
    main()

