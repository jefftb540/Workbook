from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.model):
	"""docstring for Categoria"""
	nome = models.CharField(max_length=50)
	def __init__(self, arg):
		super(Categoria, self).__init__()
		self.arg = arg
		