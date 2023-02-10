from django.urls import path

from .views import index, buscar, detalles, crear, eliminar,editar

app_name = "core"

urlpatterns = [
    path('', index, name="inicio"),
    path('buscar/', buscar, name="search"),
    path('detalles/<int:id_pelicula>', detalles, name="detail"),
    path('crear/', crear, name="create"),
    path('eliminar/<int:id_pelicula>', eliminar, name="delete"),
    path('editar/<int:id_pelicula>', editar, name="update"),
]
