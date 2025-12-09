from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    # --- Relacionamento (Apostila 1) ---
    # Alteração Temporária: null=True/blank=True até chegarmos na aula de Login
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário',
        null=True,   
        blank=True   
    )
    
    # --- Campos Básicos (Apostila 1) ---
    titulo = models.CharField(max_length=200, verbose_name='Título')
    concluida = models.BooleanField(default=False, verbose_name='Concluída')
    criada_em = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')

    # --- Campos dos Exercícios ---
    
    # Apostila 1: Descrição Opcional
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    
    # Apostila 2: Prioridade e Prazo
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    prioridade = models.CharField(
        max_length=10, 
        choices=PRIORIDADE_CHOICES, 
        default='media',
        verbose_name='Prioridade'
    )
    prazo = models.DateField(verbose_name="Prazo de Conclusão", null=True, blank=True)
    
    # Apostila 3: Data Real de Conclusão (Automática)
    data_conclusao = models.DateTimeField(null=True, blank=True, verbose_name='Data de Conclusão')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']

    def __str__(self):
        # Mostra um "check" se estiver concluída
        return f"{self.titulo} ({'✓' if self.concluida else '✗'})"