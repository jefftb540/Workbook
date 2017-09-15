
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.timezone import now



class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
       
    	user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
       
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Usuario(AbstractBaseUser, PermissionsMixin):
	"""docstring for ClassName"""
	objects = UsuarioManager()
	
	nome = models.CharField(max_length=30)
	email = models.EmailField(max_length=30, unique=True)
	facebook_name = models.CharField(max_length=30)
	facebook_ID = models.CharField(max_length=30)
	imagem = models.ImageField(null=True, blank=True)
	mediaAvaliacoes = models.IntegerField(default=0)
	totalAvaliacoes = models.IntegerField(default=0)
	nome_fantasia = models.CharField(max_length=30, default="")
	descricao = models.TextField(default="")

	#is_superuser = models.BooleanField(default=False)
	USERNAME_FIELD = "email"

	def get_full_name(self):
		return self.nome

	def get_short_name(self):
		return self.nome

	@property
	def is_superuser(self):
		return True
	@property
	def is_staff(self):
		return True
	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
		

class Categoria(models.Model):
	nome = models.CharField(max_length=60)

	def __str__(self):
		return self.nome


class SubCategoria(models.Model):
	categoria = models.ForeignKey(Categoria)
	nome = models.CharField(max_length=60)

	def __str__(self):
		return self.nome


class Servico(models.Model):
	"""docstring for Servico"""
	titulo = models.CharField(max_length=100)
	usuario = models.ForeignKey(Usuario, default=1)
	categoria =  models.ForeignKey(Categoria)
	descricao = models.TextField()
	valor_minimo = models.IntegerField(null=True)
	valor_maximo = models.IntegerField(null=True)
	imagem = models.ImageField(null=True, blank=True)
	patrocinado = models.BooleanField(default=False)
	
	def __str__(self):
		return self.titulo

		
class Avaliacao(models.Model):
	
	#servico = models.ForeignKey(Servico)
	prestador = models.ForeignKey(Usuario, related_name="Prestador")
	comentario = models.CharField(max_length=200)
	avaliador = models.ForeignKey(Usuario)
	nota = models.IntegerField()

	def __str__(self):
		return self.comentario
	"""docstring for ClassName"""

class Solicitacao(models.Model):
	
	data = models.DateTimeField(default=now, null=True)
	descricao = models.CharField(max_length=1000, null=True)
	servico = models.ManyToManyField(Servico)
	prestador = models.ForeignKey(Usuario, related_name="prestador")
	usuario = models.ForeignKey(Usuario)
	status = models.CharField(default="pendente", max_length=10)

	def __str__(self):
		return str(self.id)
		
class Orcamento(models.Model):
	"""docstring for Orcamento"""
	solicitacao = models.ForeignKey(Solicitacao)
	descricao = models.CharField(max_length=1000, default="", blank=True)
	validade = models.DateTimeField(null=True)
	#data e hora de atendimento
	servicos_atendidos = models.ManyToManyField(Servico)
	valor = models.IntegerField(default=0)
	#status (cancelado, pedente, confirmado, concluido, avaliado)
	status = models.CharField(max_length=10,default="pendente", choices=[['cancelado','Cancelado'],['pendente','Pendente'],['confirmado','Confirmado'], ['concluido','Concluido'], ['avaliado', 'Avaliado']])

class Notificacao(models.Model):
	"""docstring for notificacao"""
	tipo = models.CharField(max_length=100)
	solicitacao = models.ForeignKey(Solicitacao)
	lida = models.BooleanField(default=False)
		
class Mensagem(models.Model):
	"""docstring for mensagem"""
	solicitacao = models.ForeignKey(Solicitacao)
	usuario = models.ForeignKey(Usuario)
	texto = models.CharField(max_length=350)
	def __str__(self):
		return self.texto
	
