from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'get_user_email', 'concluida', 'criada_em', 'project')
    list_filter = ('concluida', 'user', 'criada_em', 'project')
    
    # DICA EXTRA: Em search_fields, use 'project__titulo' em vez de apenas 'project'
    # para buscar pelo nome do projeto, senão pode dar erro de busca.
    search_fields = ('titulo', 'user__username', 'project__titulo')

    fieldsets = (
        ('Informações Principais', {
            # ADICIONEI 'project' AQUI EMBAIXO:
            'fields': ('user', 'titulo', 'project')
        }),
        ('Status da Tarefa', {
            'fields': ('concluida', 'criada_em')
        }),
    )

    readonly_fields = ('criada_em',)

    @admin.display(description='Email do Usuário') 
    def get_user_email(self, obj):
        return obj.user.email

admin.site.register(Tarefa, TarefaAdmin)