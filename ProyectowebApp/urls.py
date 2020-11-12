from django.urls import path
from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name="Home"),
    path('contacto', views.contacto, name="Contacto"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)