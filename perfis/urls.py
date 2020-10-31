from django.urls import path
from perfis import views

urlpatterns = [
    path('', views.timeline, name='index'),
    path('perfil/', views.contatos, name='contatos'),
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
    path('publicar/', views.PublicarPostView.as_view(), name='publicar'),
    path('minha-timeline/', views.timeline_pessoal, name='timeline_pessoal'),
    path('perfil/<int:perfil_id>/timeline/', views.timeline_amigo, name='timeline_amigo')
]
