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
                return render(request, 'app/admin.html', {'usuarioo' : usuario_actual[0]})

            miembros = models.Cuenta.objects.all()

            if es_miembro(usuario, contrasenia, miembros):
                usuario_actual[0] = usuario
                return render(request, 'app/eleccion.html', {'usuarioo' : usuario_actual[0]})
            
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

            return render(request, 'app/admin.html', {'usuarioo' : usuario_actual[0]})
            
    return render(request, 'app/agregar.html', {'usuarioo' : usuario_actual[0]})

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

def ver_foda(request):


    fodas = models.FodaPersonal.objects.all()

    fodas_del_usuario = []

    for foda in fodas:

        if foda.miembro == usuario_actual[0]:

            fodas_del_usuario.append(foda)
    
    return render(request, 'app/verFoda.html', {'fodas' : fodas_del_usuario})


def ver_fodas(request):

    fodas = models.FodaPersonal.objects.all()

    return render(request, 'app/verFodas.html', {'fodas' : fodas})


def chat1(request):

    mensajes = models.Mensaje.objects.all()

    if request.method == 'GET':

        return render(request, 'app/chat1.html', {'mensajes' : mensajes})

    elif request.method == 'POST':

        miMensaje = forms.Mensaje(request.POST)

        # print(miMensaje)
        # t = miMensaje + 'hola'
        t = miMensaje.__str__()
        if miMensaje.is_valid:

            contenido = miMensaje.cleaned_data

            mensaje = models.Mensaje(miembro=usuario_actual[0], mensaje=contenido['mensaje'])


            mensaje.save()

            # mensaje.clean()

            miMensaje.clean()


    request.method = 'GET'
    
    return render(request, 'app/chat1.html', {'mensajes' : mensajes})

def chat2(request):

    mensajes = models.Mensaje.objects.all()

    if request.method == 'GET':

        return render(request, 'app/chat2.html', {'mensajes' : mensajes})

    elif request.method == 'POST':

        miMensaje = forms.Mensaje(request.POST)

        print(miMensaje)

        if miMensaje.is_valid:

            contenido = miMensaje.cleaned_data
            if usuario_actual[0] is None:
                usuario_actual[0] = 'lautaro'
            mensaje = models.Mensaje(miembro=usuario_actual[0], mensaje=contenido['mensaje'])

            mensaje.save()

    return render(request, 'app/chat2.html', {'mensajes' : mensajes})