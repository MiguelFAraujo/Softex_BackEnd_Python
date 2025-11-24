from django.contrib import admin
from .models import Tarefa
# 1. Crie uma classe que herda de admin.ModelAdmin
# A convenção é usar o nome do Model + "Admin"
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user',  'get_user_email', 'concluida', 'criada_em')
# Adiciona uma barra lateral de filtros
# O Django entende o tipo de campo e cria o filtro certo:
# - 'concluida': Filtro de "Sim/Não"
# - 'user': Filtro de lista (baseado em um ForeignKey)
# - 'criada_em': Filtro de data (Hoje, Últimos 7 dias, Este mês, etc.)
    list_filter = ('concluida', 'user', 'criada_em')
    search_fields = ('titulo', 'user__username')
    fieldsets = (
        ('Informações Principais', {
        'fields': ('user', 'titulo')
        }),
        ('Status da Tarefa', {
        'fields': ('concluida', 'criada_em')
        }),
        )
        # 'readonly_fields' define campos que podem ser vistos, mas não editados
        # Perfeito para campos automáticos como 'criada_em'
    readonly_fields = ('criada_em',)

    @admin.display(description='Email do Usuário') # Define o título da coluna
    def get_user_email(self, obj):
         return obj.user.email



admin.site.register(Tarefa, TarefaAdmin)
