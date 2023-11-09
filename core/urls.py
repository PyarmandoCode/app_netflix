from django.urls import path,include
from . import views

from rest_framework import routers #API FULL
router = routers.DefaultRouter() # GET,PUT,POST,DELETE
router.register('full_movies',views.MovieFullViewset)

urlpatterns = [
    path('api/List_All_Movies',views.MovieAllViewset.as_view()),
    path('api/List_All_Person',views.PersonAllViewset.as_view()),
    path('api/List_All_Genere',views.GenerAllViewset.as_view()),
    path('api/Login',views.LoginView.as_view()),
    path('api/Alta_user',views.RegisterUser.as_view()),
    
    path('api/',include(router.urls))
]

