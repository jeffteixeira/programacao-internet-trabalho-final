from django.contrib import admin
from django.urls import path, include
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfis.urls')),
    path('registrar/', RegistrarUsuarioView.as_view(template_name='registrar.html'), name='registrar'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
