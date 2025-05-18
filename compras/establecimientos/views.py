from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EstablecimientoForm
from .models import Establecimiento
# Create your views here.
class EstablecimientoListView(ListView):
    model = Establecimiento
    template_name = 'establecimientos/lista_establecimientos.html'

class EstablecimientoCreateView(CreateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'establecimientos/form_establecimiento.html'
    success_url = reverse_lazy('establecimientos:lista')

class EstablecimientoUpdateView(UpdateView):
    model = Establecimiento
    form_class = EstablecimientoForm
    template_name = 'establecimientos/form_establecimiento.html'
    success_url = reverse_lazy('establecimientos:lista')

class EstablecimientoDeleteView(DeleteView):
    model = Establecimiento
    template_name = 'establecimientos/eliminar_establecimiento.html'
    success_url = reverse_lazy('establecimientos:lista')