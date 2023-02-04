from django.contrib import admin
from .models import *

class PessoaCustomizado(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'funcao', 'ativo', )

admin.site.register(pessoa, PessoaCustomizado)
