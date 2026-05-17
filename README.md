[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# **MARKETPLACE**

Este proyecto implementa un **Marketplace** en Python utilizando los principios fundamentales de la **Programación Orientada a Objetos (POO)**:

clases, objetos, encapsulamiento, herencia, polimorfismo, clases abstractas, modularidad y sobrecarga de operadores.

El sistema permite gestionar usuarios, productos, compras, carritos, mensajes entre usuarios y tarjetas premium con descuento.

Además, el proyecto se ha organizado siguiendo una **arquitectura por capas**, separándonoslas entidades, servicios, interfaz de usuario y punto de entrada.


---


# Funcionalidades principales

## 1. Gestión de usuarios

- Creación de usuarios con nombre, apellido y DNI válido.
- Posibilidad de tener tarjeta premium con descuento.
- Los usuarios pueden:
	- Publicar productos
	- Comprar productos
	- Enviar mensajes
	- Añadir saldo.

### Condición para la tarjeta premium
La tarjeta premium solo puede obtenerse si el usuario ha realizado **al menos 3 compras distintas**.


---

## 2. Carrito de compra

- Añadir productos al carrito.
- Vaciar carrito.
- Calcular total.
- Sobrecarga del operador `+` para combinar carritos.


---


## 3. Productos disponibles

El sistema incluye varios tipos de productos mediante **herencia**:

- `Producto`
- `ProductoRopa`
- `ProductoElectronico`
- `ProductoCoche`

Todas las clases heredan de la clase abstracta `Publicacion`.


---


## 4. Sistema de pago

Clases implementadas con herencia:

- `Pagar`
- `PagarEfectivo`
- `PagarTarjeta`

Características:

- Añadir saldo.
- Validación de fondos antes de realizar compras.


---


## 5. Conversaciones y mensajería

- Envío de mensajes entre usuarios.
- Gestión de conversaciones privadas.

Clases principales:

- `Conversacion`
- `Mensaje`


---


## 6. Tarjeta Premium

- Descuento configurable (por defecto 10%).
- Aplicación automática del descuento en las compras.
- Disponible únicamente tras completar 3 compras distintas.


---


# Estructura del proyecto

```markdown
📁 marketplace/
├── entities/
│   ├── carrito.py
│   ├── conversacion.py
│   ├── estado_producto.py
│   ├── marketplace.py
│   ├── mensaje.py
│   ├── pagar.py
│   ├── pagar_efectivo.py
│   ├── pagar_tarjeta.py
│   ├── persona.py
│   ├── producto.py
│   ├── producto_coche.py
│   ├── producto_electronico.py
│   ├── producto_ropa.py
│   └── publicacion.py
│
├── services/
│   ├── gestion_marketplace_service.py
│   ├── gestion_usuarios_service.py
│   ├── gestion_productos_service.py
│   ├── gestion_conversaciones_service.py
│   └── seed_data_service.py
│
├── ui/
│   └── menu.py
│
├── tests/
│   ├── test_persona.py
│   ├── test_producto.py
│   ├── test_carrito.py
│   └── test_tarjeta_premium.py
│
├── main.py
└── README.md

```


---


# Instalación

Este proyecto **no requiere librerías externas**.

## Requisitos

- Python 3.10 o superior


## 

## Clonar el repositorio

```bash
git clone https://github.com/prog2-ia/trabajo-final-a3
```

## Acceder al proyecto

```bash
cd trabajo-final-a3
```


## Ejecutar el programa

```bash
python main.py
```

---


# Ejecución y pruebas

El sistema funciona mediante un menú interactivo (`MenuCLI`) que permite:

- Registrar usuarios
- Publicar productos
- Listar productos
- Comprar productos
- Buscar por título o tipo
- Iniciar conversaciones
- Enviar mensajes
- Solicitar tarjeta premium


---


# Principios de POO aplicados

## 1. Encapsulamiento

Uso de atributos privados mediante `_atributo`.

## 2. Herencia

Aplicada en clases como:

- `ProductoRopa`
- `ProductoCoche`
- `PagarTarjeta`

## Polimorfismo

Sobrescritura de métodos como:

- `__str__`
- `comprar()`
- `mostrar_info()`

## Clases abstractas

Las clases `Publicacion` y `Pagar` definen comportamientos obligatorios para sus subclases.

## Modularidad

Separación del proyecto en capas y archivos independientes.

## Sobrecarga de operadores

La clase `Carrito` implementa:

- `+`
- `len()`


---


# Trabajo en equipo y GitHub

- Commits frecuentes y descriptivos.
- Uso correcto de ramas y merges.
- Reparto equilibrado de tareas.


# Licencia

Proyecto académico. 

Uso libre con fines educativos y de aprendizaje.

