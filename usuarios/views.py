from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.shortcuts import redirect
from usuarios.forms import RegistrarUsuarioForm
from perfis.models import Perfil


class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)


    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            usuario = User(username=cleaned_data['nome'], email=cleaned_data['email'])
            usuario.set_password(cleaned_data['senha'])
            usuario.save()

            Perfil.objects.create(
                nome=cleaned_data['nome'],
                telefone=cleaned_data['telefone'],
                nome_empresa=cleaned_data['nome_empresa'],
                usuario=usuario
            )
            return redirect('index')
        return render(request, self.template_name, {'form': form})
