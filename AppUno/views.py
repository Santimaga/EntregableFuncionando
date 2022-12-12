from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
# Create your views here.

def inicio(request):
    return HttpResponse("Hola desde Django")


def familiar(request):
    familiar1 = Familiar( nombre = "Eduardo",edad = 70, nacimiento = "1952-12-18", rol= "Padre")
    familiar1.save()
    familiar2 = Familiar( nombre = "Andrea",edad = 55, nacimiento = "1967-04-28", rol= "Madre")
    familiar2.save()
    familiar3 = Familiar( nombre = "Santiago",edad = 27, nacimiento = "1995-10-28", rol= "Yo")
    familiar3.save()
    familiar4 = Familiar( nombre = "Gonzalo",edad = 24, nacimiento = "1998-05-21", rol= "Hermano")
    familiar4.save()
    familiar5 = Familiar( nombre = "Agustin",edad = 24, nacimiento = "1998-05-21", rol= "Hermano")
    familiar5.save()
    


    return render(request, "padre.html", {"familiar1" : familiar1 ,"familiar2" : familiar2,"familiar3" : familiar3,"familiar4" : familiar4,"familiar5" : familiar5})

