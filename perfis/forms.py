from django import forms


class CriarPostagemForm(forms.Form):
    texto = forms.CharField(required=True)

    def is_valid(self):
        valido = True
        if not super(CriarPostagemForm, self).is_valid():
            self.adicionar_erro('Verifique os dados informados')
            valido = False

        return valid

    def adicionar_erro(self, mensagem):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())

        erros.append(message)
