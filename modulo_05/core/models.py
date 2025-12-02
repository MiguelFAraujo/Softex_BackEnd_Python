from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    """
    Model para representar uma tarefa de usuário.
    """
    
    # --- CAMPOS ---
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário'
    )
    
    titulo = models.CharField(
        max_length=200, 
        verbose_name='Título'
    )
    
    concluida = models.BooleanField(
        default=False, 
        verbose_name='Concluída'
    )
    
    criada_em = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Criada em'
    )
    
    # --- METADADOS ---
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-criada_em']

    # --- MÉTODOS MÁGICOS ---
    # Note que o 'def' tem que estar na mesma linha vertical da 'class Meta'
    def __str__(self):
        """Representação em string (usado no admin)"""
        return f"{self.titulo} ({'✓' if self.concluida else '✗'})"