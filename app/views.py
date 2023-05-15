from django.shortcuts import render
from app import models, forms

usuario_actual = [None]

# Create your views here.
def es_miembro(usuario, contrasenia, miembros):
    for miembro in miembros:
        if miembro.usuario == usuario and miembro.contrasenia == contrasenia:
            return True
    return False



def login(request):
    ver_mensaje = False

    if request.method == 'POST':
        
        miFormulario = forms.Login(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            usuario = informacion['usuario']
            contrasenia = informacion['contrasenia']
        
            if usuario == 'lautaro' and contrasenia == 'osi':
                usuario_actual[0] = 'lautaro'
                return render(request, 'app/admin.html', {'usuario' : usuario, 'contrasenia' : contrasenia})

            miembros = models.Cuenta.objects.all()

            if es_miembro(usuario, contrasenia, miembros):
                usuario_actual[0] = usuario
                return render(request, 'app/eleccion.html', {'usuario' : usuario, 'contrasenia' : contrasenia})
            
            ver_mensaje = True

    return render(request, 'app/index.html', {'verMensaje' : ver_mensaje})

def agregar(request):

    if request.method == 'POST':

        miFormulario = forms.CrearCuenta(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            cuenta = models.Cuenta(usuario=informacion['usuario'], contrasenia=informacion['contrasenia'], rol=informacion['rol'])

            cuenta.save()

            return render(request, 'app/admin.html', {'usuario' : informacion['usuario'], 'contrasenia' : informacion['contrasenia']})
            
    return render(request, 'app/agregar.html')

def foda(request):
    return render(request, 'app/foda.html')

def eleccion(request):
    return render(request, 'app/eleccion.html')

def formulario(request):
    return render(request, 'app/area.html')

def admin(request):
    return render(request, 'app/admint.html')

def ver(request):
    
    miembros = models.Cuenta.objects.all()
    return render(request, 'app/miembros.html', {'miembros' : miembros})

def fodaPersonal(request):

    if request.method == 'POST':

        miFormulario = forms.Foda(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            if 'fortaleza' in informacion:
                fortaleza = informacion['fortaleza']
            else:
                fortaleza = 'null'

            if 'oportunidad' in informacion:
                oportunidad = informacion['oportunidad']
            else:
                oportunidad = 'null'
            
            if 'debilidad' in informacion:
                debilidad = informacion['debilidad']
            else:
                debilidad = 'null'
            
            if 'amenaza' in informacion:
                amenaza = informacion['amenaza']
            else:
                amenaza = 'null'

            fodaa = models.FodaPersonal(miembro=usuario_actual[0], fortaleza=fortaleza, oportunidad=oportunidad, debilidad=debilidad, amenaza=amenaza)

            fodaa.save()

            return render(request, 'app/eleccion.html')

    return render(request, 'app/fodaPersonal.html')

def ver_foda_personal(request):


    fodas = models.FodaPersonal.objects.all()

    fodas_del_usuario = []

    for foda in fodas:

        if foda.miembro == usuario_actual[0]:

            fodas_del_usuario.append(foda)
    
    return render(request, 'app/verFodaPersonal.html', {'fodas' : fodas_del_usuario})