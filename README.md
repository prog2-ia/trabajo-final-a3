[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# MARKETPLACE

Este proyecto implementa un **Marketplace** en Python utilizando los principios fundamentales de la **Programación Orientada a Objetos (POO)**:

clases, objetos, encapsulamiento, herencia, polimorfismo, clases abstractas, modularidad y sobrecarga de operadores.

El sistema permite gestionar usuarios, productos, compras, carritos, mensajes entre usuarios y tarjetas premium con descuento.


## Características principales

1. Gestión de usuarios
- Creación de usuarios con nombre, apellido y DNI válido.
- Posibilidad de tener tarjeta premium con descuento.
- Usuarios pueden:
	- Publicar productos
	- Comprar productos
	- Enviar mensajes
	- Añadir saldo.

2. Carrito de compra
- Añadir productos al carrito.
- Vaciar carrito.
- Calcular total.
- **Sobrecarga del operador +** para combinar carritos.


3. Productos disponibles
Incluye varios tipos de productos mediante **herencia**:
- Producto (base)
- ProductoRopa
- ProductoElectronico
- ProductoCoche

Todos heredan de la clase abstracta Publicacion.


4. Sistema de pago
Clases con herencia:
- Pagar
- PagarEfectivo
- PagarTarjeta

Incluye método para **añadir saldo**.


5. Conversaciones
Envío de mensajes entre usuarios.
- Clase Conversacion y Mensaje.


6. Tarjeta Premium
- Descuento configurable (por defecto 10%).
- Aplicado automáticamente en las compras.

## Estructura del proyecto
```markdown
📁 marketplace/
├── carrito.py
├── conversacion.py
├── estado_producto.py
├── market_place.py
├── mensaje.py
├── pagar.py
├── pagar_efectivo.py
├── pagar_tarjeta.py
├── persona.py
├── producto.py
├── producto_coche.py
├── producto_electronico.py
├── producto_ropa.py
├── publicacion.py
├── tarjeta_premium.py
├── requirements.txt
└── README.md
```

## Instalación
Este proyecto **no requiere librerías externas**.
Solo necesitas Python 3.10+.

1. Clona el repositorio:

	git clone https://github.com/prog2-ia/trabajo-final-a3

2. Entra en la carpeta del proyecto:

	cd trabajo-final-a3

3. Ejecuta el programa principal:

	python market_place.py

## Ejecución y pruebas
El archivo market_place.py genera:
- 10 usuarios aleatorios
- Productos base y especializados
- Pruebas de compra
- Pruebas de carrito
- Pruebas de descuento premium
- Pruebas de mensajes

Todo se muestra por consola.


## Principios de POO aplicados
1. Encapsulamiento
Atributos privados con _atributo.

2. Herencia
Clases como ProductoRopa, ProductoCoche, PagarTarjeta, etc.

3. Polimorfismo
Métodos sobrescritos como __str__, comprar, mostrar_info.

4. Clases abstractas
Publicacion define métodos obligatorios.

5. Modularidad

Cada clase en su propio archivo.


## Trabajo en equipo y GitHub
- Commits frecuentes y descriptivos.
- Reparto equilibrado de tareas.


## Licencia
Proyecto académico. Uso libre para aprendizaje.

