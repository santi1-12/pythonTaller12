from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Producto

# --- Vistas básicas usando HttpResponse ---
def index(request):
    return HttpResponse("Listado de productos")

def crear(request):
    return HttpResponse("Formulario para crear un producto")

def editar(request, id):
    return HttpResponse(f"Editar producto con id {id}")

def eliminar(request, id):
    return HttpResponse(f"Eliminar producto con id {id}")

# --- Vistas que usan templates ---
def home(request):
    """
    Muestra la lista de productos desde la base de datos.
    """
    productos = Producto.objects.all()
    return render(request, 'productos/home.html', {'productos': productos})

def detalle_producto(request, pk):
    """
    Muestra el detalle de un producto específico.
    """
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})
