from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    # User opcional (null=True) pois ainda não temos Login (Apostila 4)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário',
        null=True,   
        blank=True   
    )
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    concluida = models.BooleanField(default=False, verbose_name='Concluída')
    criada_em = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']

    def __str__(self):
        return f"{self.titulo} ({'✓' if self.concluida else '✗'})"