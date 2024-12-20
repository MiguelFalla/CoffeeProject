from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from Core.forms import ContactForm, PublicacionForm, ComentarioForm

# --- MODELOS ---

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='publicaciones/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    @property
    def comentarios(self):
        return Comentario.objects.filter(publicacion=self)


class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(
        Publicacion, on_delete=models.CASCADE, related_name='comentarios'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.publicacion}"


# --- VISTA PARA CONTACTO ---

def contact(request):
    """
    Vista para el formulario de contacto.
    Envía un correo usando Mailtrap y muestra una confirmación al usuario.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Recoger los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Componer el mensaje del correo
            asunto = f"Nuevo mensaje de {nombre} {apellido}"
            mensaje_email = (
                f"De: {nombre} {apellido}\n"
                f"Correo: {email}\n\n"
                f"Mensaje:\n{mensaje}"
            )
            destinatarios = ['a7686886074bf9@inbox.mailtrap.io']  # Mailtrap para pruebas

            try:
                # Enviar el correo
                send_mail(
                    asunto,
                    mensaje_email,
                    settings.EMAIL_HOST_USER,  # Configurado en settings.py
                    destinatarios,
                    fail_silently=False,  # Muestra errores si falla el envío
                )
                # Confirmación de envío
                return render(
                    request, 'Core/contact.html',
                    {'form': ContactForm(), 'success': True}
                )
            except Exception as e:
                # Muestra error si ocurre algún problema
                return render(
                    request, 'Core/contact.html',
                    {'form': form, 'error': f"Error al enviar el correo: {e}"}
                )

    else:
        form = ContactForm()

    return render(request, 'Core/contact.html', {'form': form})
