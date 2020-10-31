from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()

    def obter_timeline(self):
        return Post.objects.filter(profile=self).order_by('-criado_em')

    def __str__(self):
        return f'{self.nome}({self.usuario.username})'


class Convite(models.Model):
    solicitante = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='convites_feitos'
    )

    convidado = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='convites_recebidos'
    )

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()


class Postagem():
    texto = models.TextField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)


    def __str__(self):
        return f'Postagem {self.profile.nome} - {self.created_at}'
