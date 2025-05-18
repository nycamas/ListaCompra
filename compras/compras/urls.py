from django.contrib import admin
from django.urls import path, include
from lista_compra.views import InicioView  # Importa la vista basada en clase correctamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),  # Usa la vista basada en clase
    path('usuarios/', include('usuarios.urls')),
    path('establecimientos/', include('establecimientos.urls')),
    path('lista/', include('lista_compra.urls')),
]

