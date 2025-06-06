from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product


# Create your views here.
def index(request):
    productos = Product.objects.all()
    context = {"productos": productos, "categorias": Product.Category.choices}
    return render(request, "productos/list_products.html", context)


def add_new_product(request):
    product_name = request.POST["product_name"]
    product_price = request.POST["product_price"]
    product_category = request.POST["product_category"]
    Product.objects.create(
        product_name=product_name,
        valor_unitario=product_price,
        categoria=product_category
    )
    messages.success(request, "producto agregado")
    return redirect("/productos/")