#region Libreria referente a django
from django.http import HttpResponse
#endregion

#region Libreria referente a modelos
from .models import Movie,Person,Genre
from django.contrib.auth.models import User #tabla user
from django.contrib.auth import authenticate
#endregion

#region Libreria referente a DRF
from rest_framework import generics,viewsets
from rest_framework.authtoken.models import Token #tabla token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
#endregion

#region Libreria referente a serializer
from .serializers import MovieSerializer,PersonSerializer,GenerSerializer
import json
#endregion

class MovieAllViewset(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class GenerAllViewset(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset=Genre.objects.all()
    serializer_class=GenerSerializer  

class PersonAllViewset(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

#Esta clase me genera un metodo RESTFULL
class MovieFullViewset(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        username=request.data["username"]
        password=request.data["password"]
        user=authenticate(username=username,password=password)
        if user:
            #select * from token where user_id=user.id
            token=Token.objects.get(user_id=user.id)
            data = {
                "nombre":user.first_name,
                "apellido":user.last_name,
                "correo":user.email,
                "token":token.key
                
            }
        else:
            data={"error":"Credenciales Invalidas"}    
        rpta=json.dumps(data) 
        return HttpResponse(rpta,content_type="application/json")   

class RegisterUser(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        username = request.data['username']
        email=request.data['email']
        password=request.data['password']
        first_name=request.data['firstname']
        last_name=request.data['lastname']
        user = User.objects.create_user(username,email,password)

        user.first_name=first_name
        user.last_name=last_name
        user.save()
        token=Token.objects.create(user=user)
        data = {
            'msj':'User Ok con token' + token.key
        }
        rpta=json.dumps(data)
        return HttpResponse(rpta,content_type='application/json')

        




        






    
    
