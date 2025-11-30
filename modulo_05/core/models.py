from django.db import models 
from django.contrib.auth.models import User 

class Tarefa(models.Model): 
    # Foreign Key: garante que toda Tarefa pertença a um Usuário 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=200) 
    concluida = models.BooleanField(default=False) 
    criada_em = models.DateTimeField(auto_now_add=True) 
    def str  (self): 
        return self.titulo