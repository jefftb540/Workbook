# -*- coding: utf-8 -*-
from rest_framework import  serializers
from models import Notificacao, Categoria, SubCategoria, Usuario, Servico, Orcamento, Solicitacao, Mensagem, Avaliacao
from drf_extra_fields.fields import Base64ImageField


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'

class SubCategoriaSerializer(serializers.ModelSerializer):
	categoria = serializers.StringRelatedField()
	class Meta:
		model = SubCategoria
		fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
	imagem= Base64ImageField()
	class Meta:
		model = Usuario
		fields = '__all__'

class UsuarioSerializerNoPassword(serializers.ModelSerializer):
    password = serializers.ReadOnlyField()
	imagem= Base64ImageField()
	class Meta:
		model = Usuario

class UserCreateSerializer(serializers.ModelSerializer):
	imagem= Base64ImageField()
	def create(self, validated_data):
		instance = Usuario.objects.create_user(**validated_data)
		return instance

	class Meta:
	    model = Usuario
	    fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):

	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
	imagem = Base64ImageField()
	class Meta(object):
		model = Servico
		fields = '__all__'

class ServicoSerializerGet(serializers.ModelSerializer):

	usuario = UsuarioSerializer(read_only=True)
	categoria = CategoriaSerializer(read_only=True)
	imagem = Base64ImageField()
	class Meta(object):
		model = Servico
		fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
	avaliador = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	prestador = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	#servico = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())
	class Meta:
		model = Avaliacao
		fields = '__all__'


class AvaliacaoSerializerGet(serializers.ModelSerializer):
	avaliador = UsuarioSerializer()
	prestador = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	#servico = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())
	class Meta:
		model = Avaliacao
		fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	prestador = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	servico = serializers.PrimaryKeyRelatedField(many=True, queryset=Servico.objects.all())
	#data = serializers.DateTimeField(format="%d/%m/%Y")


	class Meta:
		model = Solicitacao
		fields = '__all__'

class SolicitacaoSerializerGet(serializers.ModelSerializer):
	usuario = UsuarioSerializer(read_only=True)
	prestador = UsuarioSerializer(read_only=True)
	servico = ServicoSerializer(many=True, read_only=True)
	#data = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)

	class Meta:
		model = Solicitacao
		fields = '__all__'


class OrcamentoSerializer(serializers.ModelSerializer):
	solicitacao = serializers.PrimaryKeyRelatedField(queryset=Solicitacao.objects.all())
	servicos_atendidos = serializers.PrimaryKeyRelatedField(many=True, queryset=Servico.objects.all())

	class Meta:
		model = Orcamento
		fields = '__all__'

class OrcamentoSerializerGet(serializers.ModelSerializer):
	solicitacao = SolicitacaoSerializerGet(read_only=True)
	servicos_atendidos = ServicoSerializer(many=True, read_only=True)
	data_atendimento = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)

	class Meta:
		model = Orcamento
		fields = '__all__'




class MensagemSerializerGet(serializers.ModelSerializer):
	usuario = UsuarioSerializer(read_only=True)
	solicitacao = SolicitacaoSerializer(read_only=True)
	class Meta:
		model = Mensagem
		fields = '__all__'


class MensagemSerializerList(serializers.ModelSerializer):
	solicitacao = serializers.PrimaryKeyRelatedField(queryset=Solicitacao.objects.all())
	class Meta:
		model = Mensagem
		fields = 'solicitacao',

class MensagemSerializer(serializers.ModelSerializer):
	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	solicitacao = serializers.PrimaryKeyRelatedField(queryset=Solicitacao.objects.all())
	class Meta:
		model = Mensagem
		fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
	solicitacao = serializers.PrimaryKeyRelatedField(queryset=Solicitacao.objects.all())


	class Meta:
		model = Notificacao
		fields = '__all__'