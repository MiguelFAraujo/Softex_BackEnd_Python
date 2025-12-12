from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    # OBRIGATÓRIO: Sem null=True e sem blank=True
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tarefas',
        verbose_name='Usuário'
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo