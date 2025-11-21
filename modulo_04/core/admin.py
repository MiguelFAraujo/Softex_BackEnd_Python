from django.contrib import admin 
from .models import Tarefa 
# 1. Crie uma classe que herda de admin.ModelAdmin 
# A convenção é usar o nome do Model + "Admin" 
class TarefaAdmin(admin.ModelAdmin): 
# Por enquanto, ela está vazia. Vamos configurar aqui dentro. 
    list_display = ('titulo', 'user', 'concluida', 'criada_em')
    list_filter = ('concluida', 'criada_em')
    search_fields = ('titulo', 'user__username')

    fieldsets = ( 
    # 'fieldsets' permite agrupar os campos em seções 
    # A estrutura é: ( ('Nome da Seção', {'fields': ('campo1', 'campo2')}) , ... ) 
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

    # 2. Defina o método 
# O 'obj' é a instância da Tarefa que está sendo exibida na linha 
    @admin.display(description='Email do Usuário') # Define o título da coluna 
    def get_user_email(self, obj): 
        return obj.user.email 
# 2. Modifique o registro 
# Em vez de registrar 'Tarefa' sozinho, 
# registre 'Tarefa' COM a sua classe de configuração 'TarefaAdmin' 
admin.site.register(Tarefa, TarefaAdmin) 