"""workbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from servico.views import ListServicos, ListServicosPorPrestador, GetServico, ListUsuarios, GetUsuario, GetRequestUser, ListCategorias, GetCategoria, ListSubCategorias, GetSubCategoria, ListSolicitacoes, GetSolicitacao, AddSolicitacao, AddOrcamento,ListOrcamentos, GetOrcamento, GetAvaliacoesServico, AddAvaliacao, login

router = routers.SimpleRouter()

urlpatterns = [
	
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^servicos/all', ListServicos.as_view()),
    url(r'^servicos/(\d+)$', GetServico.as_view()),
    url(r'^servicos/prestador/(\d+)$', ListServicosPorPrestador.as_view()),
    url(r'^servicos/avaliacoes/(\d+)$', GetAvaliacoesServico.as_view()),
    url(r'^servicos/avaliacoes/criar', AddAvaliacao.as_view()),
    url(r'^usuarios/all', ListUsuarios.as_view()),
    url(r'^usuarios/(\d+)$', GetUsuario.as_view()),
    url(r'^usuarios/ativo', GetRequestUser.as_view()),
    url(r'^categorias/all', ListCategorias.as_view()),
    url(r'^categorias/(\d+)$', GetCategoria.as_view()),
    url(r'^subcategorias/all', ListSubCategorias.as_view()),
    url(r'^subcategorias/(\d+)$', GetSubCategoria.as_view()),
    url(r'^solicitacoes/all', ListSolicitacoes.as_view()),
    url(r'^servicos/solicitacoes/criar', AddSolicitacao.as_view()),
    url(r'^servicos/solicitacoes/(\d+)$', GetSolicitacao.as_view()),
    url(r'^orcamentos/all', ListOrcamentos.as_view()),
    url(r'^orcamentos/(\d+)$', GetOrcamento.as_view()),
    url(r'^servicos/orcamento/criar', AddOrcamento.as_view()),


]
