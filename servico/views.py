#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
# -*- coding: utf-8 -*-
from rest_framework.response import Response
from django.core import serializers as Serializers
from django.db.models import Q
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import login, logout
from . import models
from . import serializers
from models import Notificacao, Servico, Usuario, Avaliacao, Solicitacao, Orcamento, Categoria, SubCategoria, Mensagem
from serializers import NotificacaoSerializer, ServicoSerializer, ServicoSerializerGet, UsuarioSerializer, UsuarioSerializerNoPassword, UserCreateSerializer,CategoriaSerializer, AvaliacaoSerializer, AvaliacaoSerializerGet, SolicitacaoSerializer, SolicitacaoSerializerGet, OrcamentoSerializer, OrcamentoSerializerGet, MensagemSerializer, MensagemSerializerGet, MensagemSerializerList
from oauth2_provider.views.generic import ProtectedResourceView
from django.forms.models import modelform_factory
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from base64 import b64decode
from django.core.files.base import ContentFile
from django.http import JsonResponse


import uuid
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ApiEndpoint(ProtectedResourceView):
	"""docstring for ApiEndpoint"""
	def get(self, request, *args, **kwargs):
		return HttpResponse("Protegido com OAuth2")


class SaveServico(APIView):
	def post(self, request, format=None):
		instance = ServicoSerializer(data=request.data)
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			ServicoSerializer.save(instance)
		else:
			print instance.errors

		return Response(instance.data)

class UpdateServico(APIView):

	def post(self, request, format=None):
		instance = Servico.objects.get(pk=request.data.get('id'))
		print instance
		servico = ServicoSerializerGet(instance=instance, data=request.data, partial=True)
		#print servico
		#print vars(request.POST.get(["nota"]))
		if servico.is_valid():
			print "válido"
			ServicoSerializerGet.save(servico)
		else:
			print servico.errors

		return Response(servico.data)

class ListServicos(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		servicos = Servico.objects.all()
		response = ServicoSerializer(servicos, many=True)
		return Response(response.data)

class DeleteServico(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		servico = Servico.objects.get(pk=self.args[0])
		servico.delete()
		return Response("Deletado")

class ListServicosPorPrestador(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		servicos = Servico.objects.filter(usuario__id=self.args[0])
		response = ServicoSerializer(servicos, many=True)
		return Response(response.data)

class GetServico(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		servico = Servico.objects.get(pk=self.args[0])
		response = ServicoSerializerGet(servico)

		return Response(response.data)

class AddUsuario(APIView):
	permission_classes = []
	def post(self, request, format=None):
		instance = UserCreateSerializer(data=request.data)
		resposta = ""
		if instance.is_valid():
			instance2 = Usuario.objects.create_user(request.data.get('email'), request.data.get('password'))
			request.data.pop('password', None)
			usuario = UsuarioSerializerNoPassword(instance=instance2, data=request.data, partial=True)
			if usuario.is_valid():
				UsuarioSerializerNoPassword.save(usuario)
				resposta = "Cadastrado"
			else:
				print usuario.errors
				resposta = "Problema nas informações extras"

		else:
			print instance.errors
			resposta = "Não cadastrado"

		return Response(resposta)


class ListUsuarios(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		usuarios = Usuario.objects.all()
		response = UsuarioSerializer(usuarios, many=True)
		return Response(response.data)

class SearchUsuarios(APIView):
	#authentication_classes = (authentication.TokenAuthentication)
	def post(self, request, format=None):
		servicos = Servico.objects.filter(Q(descricao__icontains=request.data.get("query"))|Q(titulo__icontains=request.data.get("query")))
		response = ServicoSerializerGet(servicos, many=True)
		return Response(response.data)

class GetRequestUser(APIView):
	"""docstring for GetRequestUser"""
	def get(self, request, format=None):
		return Response(UsuarioSerializer(request.user).data)

class GetUsuario(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		usuario = Usuario.objects.get(pk=self.args[0])
		response = UsuarioSerializer(usuario)
		return Response(response.data)


class GetAvaliacoesUsuario(APIView):
	#authentication_classes = (authentication.TokenAuthentication)
	def get(self, request, format=None):

		avaliacoes = Avaliacao.objects.filter(prestador=self.args[0])
		response = AvaliacaoSerializerGet(avaliacoes, many=True)
		return Response(response.data)

class AddAvaliacao(APIView):
	def post(self, request, format=None):
		instance = AvaliacaoSerializer(data=request.data)
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			AvaliacaoSerializer.save(instance)
		else:
			print "invalido"

		return Response(instance.data)

class ListCategorias(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		categorias = Categoria.objects.all()
		response = CategoriaSerializer(categorias, many=True)
		return Response(response.data)

class GetCategoria(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		categoria = Categoria.objects.get(pk=self.args[0])
		response = ServicoSerializer(categoria)
		return Response(response.data)


class ListSubCategorias(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		subCategorias = SubCategoria.objects.all()
		response = SubCategoriaSerializer(subCategorias, many=True)
		return Response(response.data)

class GetSubCategoria(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		subCategoria = SubCategoria.objects.get(pk=self.args[0])
		response = SubCategoriaSerializer(subCategoria)
		return Response(response.data)

class AddSolicitacao(APIView):
	def post(self, request, format=None):
		instance = SolicitacaoSerializer(data=request.data)
		print request.data
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			#print instance
			solicitacao = SolicitacaoSerializer.save(instance)
			notificacao = {'tipo': "Nova Solicitacao", 'solicitacao': solicitacao.id }
			notificacaoInstance = NotificacaoSerializer(data=notificacao)
			print notificacaoInstance
			if notificacaoInstance.is_valid():
				print "Notificação válida"
				NotificacaoSerializer.save(notificacaoInstance)
			else:
				print notificacaoInstance.errors

		else:
			print "invalido\n"
			print instance.errors

		return Response(instance.data)


class UpdateSolicitacao(APIView):
	def post(self, request, format=None):
		instance = Solicitacao.objects.get(pk=request.data.get('id'))
		solicitacao = SolicitacaoSerializerGet(instance=instance, data=request.data, partial=True)
		print request.data
		#print vars(request.POST.get(["nota"]))
		if solicitacao.is_valid():
			print "válido"
			SolicitacaoSerializerGet.save(solicitacao)

		else:
			print "invalido\n"
			print solicitacao.errors

		return Response(solicitacao.data)


class ListSolicitacoesPendentes(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		solicitacoes = Solicitacao.objects.filter(servico__usuario = request.user, status = "pendente").order_by('-data')
		response = SolicitacaoSerializerGet(solicitacoes, many=True)
		return Response(response.data)

class ListSolicitacoes(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		solicitacoes = Solicitacao.objects.filter(usuario = request.user).order_by('-data')
		response = SolicitacaoSerializerGet(solicitacoes, many=True)
		return Response(response.data)


class GetSolicitacao(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		solicitacao = Solicitacao.objects.get(pk=self.args[0])
		response = SolicitacaoSerializerGet(solicitacao)
		return Response(response.data)

class UpdateOrcamento(APIView):
	def post(self, request, format=None):
		instance = Orcamento.objects.get(pk=request.data.get('id'))
		orcamento = OrcamentoSerializerGet(instance=instance, data=request.data)
		print instance
		#print vars(request.POST.get(["nota"]))
		if orcamento.is_valid():
			print "válido"
			OrcamentoSerializerGet.save(orcamento)
		else:
			print orcamento.errors

		return Response(orcamento.data)

class AddOrcamento(APIView):
	def post(self, request, format=None):
		orcamento = OrcamentoSerializer(data=request.data)
		notificacao = {'tipo': "Solicitação respondida", 'solicitacao': request.data.get('solicitacao') }
		print request.data.get('solicitacao')

		#print vars(request.POST.get(["nota"]))
		if orcamento.is_valid():
			print "válido"
			OrcamentoSerializer.save(orcamento)
			notificacaoInstance = NotificacaoSerializer(data=notificacao)
			if notificacaoInstance.is_valid():
				print "Notificação válida"
				NotificacaoSerializer.save(notificacaoInstance)
			else:
				print "Notificação inválida"
		else:
			print orcamento.errors

		return Response(orcamento.data)

#aplicar a logica de negócios para pegar somente os orçamentos para o prestador
class ListOrcamentos(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		orcamentos = Orcamento.objects.filter(solicitacao__prestador = request.user)
		response = OrcamentoSerializerGet(orcamentos, many=True)
		return Response(response.data)

class GetOrcamento(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		orcamento = Orcamento.objects.get(pk=self.args[0])
		response = OrcamentoSerializerGet(orcamento)
		return Response(response.data)

class GetOrcamentoPorSolicitacao(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		orcamento = Orcamento.objects.filter(solicitacao__id=self.args[0]).order_by('-id')[0]
		response = OrcamentoSerializerGet(orcamento)
		return Response(response.data)


#Definir um meio de filtrar as mensagens por servico





class ListMensagens(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		mensagens = Mensagem.objects.filter(solicitacao_id=self.args[0])
		response = MensagemSerializerGet(mensagens, many=True)
		return Response(response.data)

class AddMensagem(APIView):
	def post(self, request, format=None):
		instance = MensagemSerializer(data=request.data)
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			MensagemSerializer.save(instance)
		else:
			print "invalido\n"
			print instance.errors

		return Response(instance.data)


class CountNotificacoes(APIView):
	"""docstring for CountNotificacoes"""
	def get(self, request, format=None):
		prestador = Notificacao.objects.filter(solicitacao__prestador=request.user.id, lida=False, tipo__icontains="Nova solicitacao").count()
		usuario = Notificacao.objects.filter(solicitacao__usuario=request.user.id, lida=False, tipo__icontains="Solicitação respondida").count()
		total = {'usuario':usuario, 'prestador':prestador}
		#response = HttpResponse(total)
		return JsonResponse(total)

class CountMensagens(APIView):
	"""docstring for CountNotificacoes"""
	def get(self, request, format=None):
		total = Mensagem.objects.filter(Q(solicitacao__usuario=request.user.id, lida=False) & ~Q(usuario=request.user.id)| Q(solicitacao__prestador=request.user.id, lida=False) & ~Q(usuario=request.user.id)).values('solicitacao').distinct().count()
		return HttpResponse(total)

class ListMensagensNaoLidas(APIView):
	"""docstring for CountNotificacoes"""
	def get(self, request, format=None):
		qs = Mensagem.objects.filter(Q(solicitacao__usuario=request.user.id, lida=False) & ~Q(usuario=request.user.id)| Q(solicitacao__prestador=request.user.id, lida=False) & ~Q(usuario=request.user.id)).order_by('solicitacao').distinct()
		anterior = -1
		for registro in qs:
			print registro.pk
			if registro.solicitacao == anterior:
				qs = qs.exclude(pk=registro.pk)
			anterior = registro.solicitacao

		mensagem = MensagemSerializerGet(list(qs), many=True)

		return JsonResponse(mensagem.data, safe=False)



class LerMensagens(APIView):
	"""docstring for CountNotificacoes"""
	def get(self, request, format=None):
		Mensagem.objects.filter(Q(solicitacao__usuario=request.user.id, lida=False, solicitacao__id=self.args[0]) & ~Q(usuario=request.user.id)| Q(solicitacao__prestador=request.user.id, lida=False, solicitacao__id=self.args[0]) & ~Q(usuario=request.user.id)).update(**{'lida':'True'})
		return HttpResponse({'Status':'Sucesso'})


class LerNotificacao(APIView):
	"""docstring for CountNotificacoes"""
	def get(self, request, format=None):
		instance = Notificacao.objects.filter(Q(solicitacao__prestador=request.user.id, solicitacao=self.args[0], lida=False)|Q(solicitacao__usuario=request.user.id, solicitacao=self.args[0], lida=False))[0]

		instance.lida = True
		instance.save()


		return HttpResponse({'Status':'Sucesso'})




"""
class GetSubCategoria(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		subCategoria = SubCategoria.objects.get(pk=self.args[0])
		response = SubCategoriaSerializer(subCategoria)
		return Response(response.data)
"""