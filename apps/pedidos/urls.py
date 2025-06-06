from django.urls import path
from . import views

app_name="pedidos"
urlpatterns = [
    path("pedidos/", views.pedidos, name="pedidos")
]