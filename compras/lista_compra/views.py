from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm

# Vista para la página de inicio
class InicioView(TemplateView):
    template_name = 'compras/inicio.html'

# Vista para listar los productos
class ListaCompraView(ListView):
    model = Producto
    template_name = 'lista_compra/lista_compra.html'
    context_object_name = 'productos'

# Vista para agregar un producto
class AgregarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'lista_compra/agregar_producto.html'
    success_url = reverse_lazy('lista_compra:lista_compra')

# Vista para editar un producto
class EditarProductoView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'lista_compra/editar_producto.html'
    success_url = reverse_lazy('lista_compra:lista_compra')

# Vista para eliminar un producto
class EliminarProductoView(DeleteView):
    model = Producto
    template_name = 'lista_compra/eliminar_producto.html'
    success_url = reverse_lazy('lista_compra:lista_compra')


