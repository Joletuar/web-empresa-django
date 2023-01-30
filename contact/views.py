from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from django.core.mail import EmailMessage # Librería que se usará para enviar los correos


# La función reverse permite pasarle un template tag como valor
# Para este caso se le pasa como parámetro el nombre para la url que se definió en las urls

# Create your views here.

# request.mehtod es una variable que contiene el tipo de método con el que se realizó la petición. Pueden ser GET o POST
# Por defecto cuando se carga una página el método usado es GET
# request.POST contiene un diccionario con los datos enviados desde el formulario

def contact(request):
    contact_form = ContactForm()
    # Verificamos que se accede a la página a traves del método POST
    if request.method == 'POST':
        # Vamos a rellenar los campos de la plantilla del formulario con los datos enviados desde el formulario a traves del método POST
        # Esto nos rellenará los campos del formulario en el front de manera automática
        contact_form = ContactForm(data=request.POST)
        # Verificamos que los campos del formulario se llenaron correctamente usando el método .is_valid que devolverá True o False
        if contact_form.is_valid():
            # Ahora recuperamos los campos
            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']
            
            # Supenemos que todo ha ido bien y redireccionamos
            
            # Vamos construir el email que se va a enviar
            email_cuerpo = EmailMessage(
                'Prueba página: Nuevo mensaje de contacto',
                f"De {name} <{email}>\n\nEscribió \n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ['joletar@gmail.com'],
                reply_to=[email]
            )
            
            # Ahora lo vamos a enviar
            try:
                email_cuerpo.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
            
    
    return render(request, 'contact/contact.html', {
        'form': contact_form
    })