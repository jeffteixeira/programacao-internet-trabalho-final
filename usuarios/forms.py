from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)


    def is_valid(self):
        valido = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Verifique os dados submetidos')
            valido = False

        usuario_ja_existe = User.objects.filter(username=self.cleaned_data['nome']).exists()
        if usuario_ja_existe:
            self.adicionar_erro('Usuário já existente')
            valido = False
        return valido


    def adicionar_erro(self, mensagem):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(mensagem)
