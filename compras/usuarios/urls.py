from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='lista'),
    path('nuevo/', views.UsuarioCreateView.as_view(), name='agregar'),
    path('editar/<int:pk>/', views.UsuarioUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', views.UsuarioDeleteView.as_view(), name='eliminar'),
]
