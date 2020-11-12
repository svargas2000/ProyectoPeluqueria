from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProyectowebApp/home.html")






def contacto(request):
    return render(request, "ProyectowebApp/contacto.html")

#class FormularioClienteView(HttpRequest):
