from django.shortcuts import render
from perfis.models import Perfil, Convite, Postagem
from django.shortcuts import redirect
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from perfis.forms import CriarPostagemForm
from django.contrib import messages


@login_required
def contatos(request):
    dados = {
        'perfis': Perfil.objects.all().exclude(usuario=request.user)
    }
    return render(request, 'contatos.html', dados)


@login_required
def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    meu_perfil = Perfil.objects.get(usuario=request.user)
    ja_eh_contato = perfil in meu_perfil.contatos.all()
    aguardando_aceitar = Convite.objects.filter(solicitante=meu_perfil, convidado=perfil)
    dados = {
        'perfil': perfil,
        'ja_eh_contato': ja_eh_contato,
        'aguardando_aceitar': aguardando_aceitar
    }
    return render(request, 'perfil.html', data)


@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    request.user.perfil.convidar(perfil_a_convidar)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


class PublicarPostView(View):
    template_name = 'publicar.html'


    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)


    @method_decorator(login_required)
    def post(self, request):
        form = CriarPostagemForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            perfil = get_object_or_404(Perfil, usuario=self.request.user)
            Postagem.objects.create(
                texto=cleaned_data['texto'],
                perfil=perfil
            )
            return redirect('index')
        return render(request, self.template_name, {'form': form})


@login_required
def timeline(request):
    dados = {
        'postagens': Post.objects.all().order_by('-criado_em'),
        'titulo': 'Timeline'
    }
    return render(request, 'timeline.html', dados)


@login_required
def timeline_pessoal(request):
    dados = {
        'postagens': Post.objects.filter(perfil__usuario=request.user).order_by('-criado_em'),
        'titulo': 'Timeline pessoal'
    }
    return render(request, 'timeline.html', data)


@login_required
def timeline_amigo(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    meu_perfil = Perfil.objects.get(usuario=request.user)
    eh_contato = perfil in meu_perfil.contatos.all()
    if not eh_contato:
        messages.info(request, 'Você só pode ver a timeline de seu contatos!')
        return redirect('index')
    dados = {
        'postagens': Post.objects.filter(perfil=perfil).order_by('-criado_em'),
        'titulo': f'Timeline {perfil.nome}'
    }
    return render(request, 'timeline.html', dados)

