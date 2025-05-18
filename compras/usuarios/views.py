from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm

# --- USUARIOS ---
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista_usuarios.html'
    context_object_name = 'usuarios' 

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioEditForm
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('usuarios:lista')

# Create your views here.
