from django.shortcuts import render
from .models import Tarefa

def home(request):
    todas_as_tarefas = Tarefa.objects.all()

    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Admin'],
        'tarefas': todas_as_tarefas
    }

    return render(request, 'home.html', context)