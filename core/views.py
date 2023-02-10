from django.shortcuts import render
from .models import peliculas, genero
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.urls import reverse


# vista basada en funcion que me permite renderizar
# a mi template(html)
def index(request):
    template_name = "index.html"
    # select * from peliculas
    pls = peliculas.objects.all()
    context = {
        "peliculas": pls
    }
    return render(request, template_name, context)


def buscar(request):
    template_name = "index.html"
    if request.method == "GET":
        # Guardando en una variable el valos del input
        query = request.GET.get('q')
        # filtrando de la tabla peliculas de acuerdo a la variable
        results = peliculas.objects.filter(Q(reseña__icontains=query) | Q(director__icontains=query))
        # creando un contexto con el resultado del filtro
        context = {
            "peliculas": results
        }
        # renderizando en el template
    return render(request, template_name, context)


def detalles(request, id_pelicula=None):
    template_name = "detalles.html"
    # select * from peliculas where id=?
    pel = peliculas.objects.get(pk=id_pelicula)
    context = {
        "pelicula": pel
    }
    return render(request, template_name, context)


def crear(request):
    template_name = "create.html"
    if request.method == "POST":
        vargenero = request.POST['genero']
        # todo creando el Objeto para el FK
        obj_genero = genero.objects.get(codgenero=vargenero)
        pelicula = peliculas(reseña=request.POST['reseña'],
                             descripcion=request.POST["descripcion"],
                             sipnosis=request.POST["sipnosis"],
                             director=request.POST["director"],
                             puntuacion=request.POST["puntuacion"],
                             # dato del FK pasarle todo el objeto
                             genero=obj_genero
                             )
        pelicula.save()
        return HttpResponseRedirect(reverse('core:inicio'))
    generos = genero.objects.all()
    context = {
        "generos": generos
    }
    return render(request, template_name, context)


def eliminar(request, id_pelicula=None):
    peliculas.objects.get(pk=id_pelicula).delete()
    return HttpResponseRedirect(reverse('core:inicio'))


def editar(request,id_pelicula):
    template_name = "edit.html"
    pelicula = peliculas.objects.get(pk=id_pelicula)

    if request.method == "POST":
        #vargenero = request.POST['genero']
        obj_genero = genero.objects.get(codgenero=1)
        # todo creando el Objeto para el FK
        pelicula.reseña=request.POST['reseña']
        pelicula.descripcion=request.POST['descripcion']
        pelicula.sipnosis=request.POST['sipnosis']
        pelicula.director=request.POST['director']
        pelicula.puntuacion=request.POST['puntuacion']
        pelicula.genero=obj_genero
        pelicula.save()
        return HttpResponseRedirect(reverse('core:inicio'))

    generos = genero.objects.all()
    context = {
        "pelicula":pelicula,
         "generos": generos
        }
    return render(request, template_name, context)

