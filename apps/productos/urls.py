from django.urls import path
from . import views

app_name="productos"
urlpatterns = [
    path("productos/", views.index, name="index"),
    path("add_product/", views.add_new_product, name="add_product"),
]