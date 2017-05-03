from rest_framework import  serializers
from models import Categoria, SubCategoria, Usuario, Servico, Orcamento, Solicitacao, Mensagem, Avaliacao


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
	class Meta:
		model = Usuario
		fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
	"""titulo = serializers.CharField(max_length=100)
	#usuario = serializers.ForeignKey(Usuario)
	#categoria =  serializers.ForeignKey(categoria)
	descricao = serializers.CharField()
	telefone = serializers.CharField(max_length=14)
	celular = serializers.CharField(max_length=14)
	imagem = serializers.FileField()
	mediaAvaliacoes = serializers.IntegerField()
	totalAvaliacoes = serializers.IntegerField()
	patrocinado = serializers.BooleanField()"""
	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	categoria = serializers.StringRelatedField()
	class Meta(object):
		model = Servico
		fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
	avaliador = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	servico = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())
	class Meta:
		depth = 1
		model = Avaliacao
		fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
	solicitacao = serializers.PrimaryKeyRelatedField(queryset=Solicitacao.objects.all())

	class Meta:
		model = Orcamento
		fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
	servico = serializers.PrimaryKeyRelatedField(many=True, queryset=Servico.objects.all())
	
	
	class Meta:
		model = Solicitacao
		fields = '__all__'

class SolicitacaoSerializerGet(serializers.ModelSerializer):
	usuario = serializers.StringRelatedField()
	servico = serializers.StringRelatedField(many=True)
	data_inicio = serializers.DateTimeField(format="%d/%m/%Y")
	data_fim = serializers.DateTimeField(format="%d/%m/%Y")

	class Meta:
		model = Solicitacao
		fields = '__all__'


class MensagemSerializer(serializers.ModelSerializer):
	usuario = serializers.StringRelatedField()
	solicitacao = serializers.StringRelatedField()
	class Meta:
		model = Mensagem
		fields = '__all__'