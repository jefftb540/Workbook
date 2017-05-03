from django.contrib import admin
from .models import Usuario
from .models import Categoria
from .models import SubCategoria
from .models import Servico
from .models import Avaliacao
from .models import Solicitacao
from .models import Orcamento
from .models import Mensagem
#from .models import Solicitacao
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Servico)
admin.site.register(Avaliacao)
admin.site.register(Solicitacao)
admin.site.register(Orcamento)
admin.site.register(Mensagem)


