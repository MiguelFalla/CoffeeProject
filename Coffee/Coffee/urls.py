"""Coffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Core import views
from django.conf import settings
from django.conf.urls.static import static
from Core.views import CustomLoginView, contact, login_view, register,login,login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name="index.html"),
    path('about/', views.about, name="about.html"),
    path('products/', views.products, name="products.html"),
    path('store/', views.store, name="store.html"),
    path('foro/', views.foro, name='foro'),
    path('editar_publicacion/<int:publicacion_id>/', views.editar_publicacion, name='editar_publicacion'),
    path('eliminar_publicacion/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion.html'),
    path('eliminar_publicacion/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion.html'),
    path('comentario/<int:publicacion_id>/', views.agregar_comentario, name='agregar_comentario.html'),
    path('eliminar_comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario.html'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Use the class-based login view,
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register.html'),
    path('category/<int:category_id>/',views.category,name="category.html"),
    path('contact/', contact, name='contact.html'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
