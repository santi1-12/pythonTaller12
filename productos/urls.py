from django.urls import path
from . import views

app_name = 'productos'  # Namespace de la app

urlpatterns = [
    path('', views.home, name='home'),                        # Página principal / listado de productos
    path('detalle/<int:pk>/', views.detalle_producto, name='detalle'),  # Detalle de un producto
    path('crear/', views.crear, name='crear'),                # Crear un producto
    path('editar/<int:id>/', views.editar, name='editar'),    # Editar un producto
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),  # Eliminar un producto
]
