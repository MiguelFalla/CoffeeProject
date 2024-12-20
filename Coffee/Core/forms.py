from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





# Formulario para la creación de un usuario personalizado
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email


# Formulario de contacto
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(max_length=100, label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


# Formulario para la creación de publicaciones


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = None  # Inicialmente dejamos esto vacío
        fields = ['titulo', 'contenido', 'categoria', 'imagen']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        # Importar el modelo dentro de __init__ para evitar la importación circular
        from .models import Publicacion
        self._meta.model = Publicacion  # Asignamos el modelo de forma explícita
        super().__init__(*args, **kwargs)


# Formulario para la creación de comentarios
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = None  # Inicialmente dejamos esto vacío
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Importar el modelo dentro de __init__ para evitar la importación circular
        from .models import Comentario
        self._meta.model = Comentario  # Asignamos el modelo de forma explícita
        super().__init__(*args, **kwargs)
