from django.urls import path
from app import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('eleccion/', views.eleccion, name='Eleccion'),
    path('foda/', views.foda, name='Foda'),
    path('formulario/', views.formulario, name='Area'),
    path('agregar/', views.agregar, name='Agregar'),
    path('admin/', views.admin, name='Admin'),
    path('ver/', views.ver, name='Ver'),
    path('fodaPersonal/', views.fodaPersonal, name='FodaPersonal'),
    path('verFodaPersonal/', views.ver_foda, name='VerFoda'),
    path('verFodaPersonales/', views.ver_fodas, name='VerFodas'),
    path('chat1/', views.chat1, name='Chat1'),
    path('chat2/', views.chat2, name='Chat2'),

]