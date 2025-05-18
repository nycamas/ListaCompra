from django.urls import path
from .views import (
    ListaCompraView, AgregarProductoView,
    EditarProductoView, EliminarProductoView
)
app_name = 'lista_compra'
urlpatterns = [
    path('', ListaCompraView.as_view(), name='lista_compra'),
    path('agregar/', AgregarProductoView.as_view(), name='agregar_producto'),
    path('editar/<int:pk>/', EditarProductoView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', EliminarProductoView.as_view(), name='eliminar_producto'),
]
