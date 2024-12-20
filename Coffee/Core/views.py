import os
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from Core.models import Publicacion, Categoria, Comentario
from Core.forms import CustomUserCreationForm, ContactForm, PublicacionForm, ComentarioForm

# --- VISTAS PRINCIPALES ---

def index(request):
    """Vista para la página principal."""
    return render(request, 'Core/index.html')

def products(request):
    """Vista para la página de productos."""
    return render(request, 'Core/products.html')

def store(request):
    """Vista para la tienda."""
    return render(request, 'Core/store.html')

def about(request):
    """Vista para la página 'Acerca de nosotros'."""
    return render(request, 'Core/about.html')

# --- FORO ---

@login_required
def foro(request):
    """Vista para mostrar las publicaciones en el foro con paginación."""
    publicaciones_list = Publicacion.objects.all().order_by('-fecha_creacion')
    paginator = Paginator(publicaciones_list, 10)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    
    return render(request, 'Core/foro.html', {'publicaciones': publicaciones})



@login_required
def crear_publicacion(request):
    """Vista para crear una nueva publicación en el foro."""
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación creada exitosamente.")
            return redirect('foro')  # Redirige a la página del foro
    else:
        form = PublicacionForm()
    return render(request, 'Core/crear_publicacion.html', {'form': form})

@login_required
def editar_publicacion(request, publicacion_id):
    """Vista para editar una publicación existente."""
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, autor=request.user)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada exitosamente.")
            return redirect('foro')
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'Core/editar_publicacion.html', {'form': form})

@login_required
def eliminar_publicacion(request, publicacion_id):
    """Vista para eliminar una publicación."""
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, autor=request.user)
    if request.method == 'POST':
        publicacion.delete()
        messages.success(request, "Publicación eliminada exitosamente.")
        return redirect('foro')
    return render(request, 'Core/eliminar_publicacion.html', {'publicacion': publicacion})

@login_required
def agregar_comentario(request, publicacion_id):
    """Vista para agregar un comentario a una publicación."""
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            comentario.save()
            messages.success(request, "Comentario agregado exitosamente.")
            return redirect('foro')
    else:
        form = ComentarioForm()
    return render(request, 'Core/agregar_comentario.html', {'form': form, 'publicacion': publicacion})

@login_required
def eliminar_comentario(request, comentario_id):
    """Vista para eliminar un comentario."""
    comentario = get_object_or_404(Comentario, id=comentario_id, autor=request.user)
    if request.method == 'POST':
        comentario.delete()
        messages.success(request, "Comentario eliminado exitosamente.")
        return redirect('foro')
    return render(request, 'Core/eliminar_comentario.html', {'comentario': comentario})

# --- REGISTRO DE USUARIOS ---

def register(request):
    """Vista para el registro de usuarios."""
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. Has iniciado sesión.")
            return redirect('index')  # Redirige a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'Core/register.html', {'form': form})

# --- CATEGORÍAS ---

def category(request, category_id):
    """Vista para filtrar publicaciones por categoría."""
    category = get_object_or_404(Categoria, id=category_id)
    publicaciones = Publicacion.objects.filter(categoria=category)
    return render(request, "Core/category.html", {'publicaciones': publicaciones, 'category': category})

# --- CONTACTO ---

def contact(request):
    """Vista para el formulario de contacto con funcionalidad de envío de correos."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']
            recipient_list = [settings.EMAIL_HOST_USER]  # Usa el correo configurado en settings
            try:
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, "Correo enviado exitosamente.")
                return redirect('contact')
            except Exception as e:
                messages.error(request, f"Error al enviar el correo: {e}")
    else:
        form = ContactForm()
    return render(request, 'Core/contact.html', {'form': form})

# --- LOGIN/LOGOUT ---

class CustomLoginView(LoginView):
    """Vista personalizada para el inicio de sesión."""
    template_name = 'Core/login.html'
    redirect_authenticated_user = True

def login_view(request):
    """Vista alternativa para el inicio de sesión."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige a la página principal
    else:
        form = AuthenticationForm()
    return render(request, 'Core/login.html', {'form': form})

def custom_logout(request):
    """Vista para cerrar sesión."""
    logout(request)
    return redirect('index')  # Redirige a la página principal
