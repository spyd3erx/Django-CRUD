from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    productos = Product.objects.all()
    context = {"productos": productos, "categorias": Product.Category.choices}
    return render(request, "productos/list_products.html", context)
