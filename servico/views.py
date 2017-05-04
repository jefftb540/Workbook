#!/usr/bin/env python
# -*- coding: utf-8 -*
from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.views import login
from . import models
from . import serializers
from models import Servico, Usuario, Avaliacao, Solicitacao, Orcamento
from serializers import ServicoSerializer, UsuarioSerializer, AvaliacaoSerializer, SolicitacaoSerializer, SolicitacaoSerializerGet, OrcamentoSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.forms.models import modelform_factory

class ApiEndpoint(ProtectedResourceView):
	"""docstring for ApiEndpoint"""
	def get(self, request, *args, **kwargs):
		return HttpResponse("Protegido com OAuth2")
		

class ListServicos(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		servicos = Servico.objects.all()
		response = ServicoSerializer(servicos, many=True)
		return Response(response.data)

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
		response = ServicoSerializer(servico)
		
		return Response(response.data)


class ListUsuarios(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		usuarios = Usuario.objects.all()
		response = UsuarioSerializer(usuarios, many=True)
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

class GetAvaliacoesServico(APIView):
	#authentication_classes = (authentication.TokenAuthentication)
	def get(self, request, format=None):

		avaliacoes = Avaliacao.objects.filter(servico=self.args[0])
		response = AvaliacaoSerializer(avaliacoes, many=True)
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
		response = ServicoSerializer(categorias, many=True)
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



#aplicar a logica de negócios para pegar somente as solicitacoes para o prestador

class AddSolicitacao(APIView):
	def post(self, request, format=None):
		instance = SolicitacaoSerializer(data=request.data)
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			SolicitacaoSerializer.save(instance) 		
		else:
			print "invalido\n"
			print instance.errors

		return Response(instance.data)
class ListSolicitacoes(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		solicitacoes = Solicitacao.objects.filter(servico__usuario = request.user)
		response = SolicitacaoSerializerGet(solicitacoes, many=True)
		return Response(response.data)

class GetSolicitacao(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		solicitacao = Solicitacao.objects.get(pk=self.args[0])
		response = SolicitacaoSerializerGet(solicitacao)
		return Response(response.data)

class AddOrcamento(APIView):
	def post(self, request, format=None):
		instance = OrcamentoSerializer(data=request.data)
		#print vars(request.POST.get(["nota"]))
		if instance.is_valid():
			print "válido"
			OrcamentoSerializer.save(instance) 		
		else:
			print instance.errors

		return Response(instance.data)

#aplicar a logica de negócios para pegar somente os orçamentos para o prestador
class ListOrcamentos(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		orcamentos = Orcamento.objects.filter(orcamento__solicitacao__servico__usuario = request.user)
		response = OrcamentoSerializer(orcamentos, many=True)
		return Response(response.data)

class GetOrcamento(APIView):
	#authentication_classes = (authentication.TokenAuthentication)

	def get(self, request, format=None):
		orcamento = Orcamento.objects.get(pk=self.args[0])
		response = OrcamentoSerializer(orcamento)
		return Response(response.data)


#Definir um meio de filtrar as mensagens por servico
"""




class ListMensagens(APIView):
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
"""