import os

# busca en la variables de entorno el entorno, en caso que no lo encuentre asume que es development
DJANGO_SETTINGS_MODULE = os.environ.get("DJANGO_SETTINGS_MODULE")

# carga la configuración de development
if DJANGO_SETTINGS_MODULE == "gestion_pedidos.settings.development":
    from .development import *
# caso contrario carga la config para produccion
elif DJANGO_SETTINGS_MODULE == "gestion_pedidos.settings.production":
    from .production import *
# genera un excepción si no reconoce el entorno
else:
    raise ImportError(f"Unknown DJANGO_SETTINGS_MODULE: {DJANGO_SETTINGS_MODULE}")
