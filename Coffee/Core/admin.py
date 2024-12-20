from django.contrib import admin
from .models import Publicacion, Comentario, Categoria

admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Categoria)
