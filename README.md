## Configurar entorno
```sh
export DJANGO_SETTINGS_MODULE=gestion_pedidos.settings.development
```
¡Perfecto! Crear un mini proyecto es una excelente forma de consolidar lo aprendido. Hasta ahora has trabajado con:

Entornos virtuales y gestión de dependencias con uv

Fundamentos de Python (estructuras, clases, funciones)

Conceptos clave de HTTP (métodos, códigos, headers)

Git y GitHub

Django: modelos, vistas, rutas, plantillas, migraciones

🎯 Objetivo del mini proyecto
Crea una app web básica de gestión de pedidos donde se pueda:

Registrar productos

Registrar pedidos

Ver el resumen de un pedido

Mostrar la factura de un pedido (cliente + total)

🧩 Estructura del proyecto
Proyecto Django: gestionpedidos

Apps:

productos → maneja los productos disponibles

pedidos → crea pedidos con productos

clientes (opcional por ahora)

🛠 Funcionalidades mínimas
Productos:

Modelo con nombre, precio unitario

Vista para listar productos

Pedidos:

Modelo con cliente, fecha, total

Modelo intermedio ItemPedido (pedido + producto + cantidad)

Vista para ver un resumen del pedido

Templates:

HTML sencillo usando variables

Mostrar totales con o sin descuento

