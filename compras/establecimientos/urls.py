from django.urls import path
from . import views

app_name = 'establecimientos'

urlpatterns = [
    path('', views.EstablecimientoListView.as_view(), name='lista'),
    path('nuevo/', views.EstablecimientoCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', views.EstablecimientoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.EstablecimientoDeleteView.as_view(), name='eliminar'),
]
