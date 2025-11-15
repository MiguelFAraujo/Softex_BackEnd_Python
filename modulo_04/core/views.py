
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm # 1. Importe o form 
from django.contrib.auth import login # 2. Importe a função 'login' 
# (Importe também seus Models e Forms de Tarefa) 
from django.contrib.auth.decorators import login_required # 1. Importe o decorador 
from .models import Tarefa 
from .forms import TarefaForm


@login_required
def home(request):

    if request.method == 'POST':
        
        form = TarefaForm(request.POST)

        if form.is_valid():

            tarefa = form.save(commit=False)
            tarefa.user = request.user
            
            tarefa.save()

            return redirect('home')
    else:

        form = TarefaForm() 

    todas_as_tarefas = Tarefa.objects.filter(user = request.user).order_by('-criada_em')

    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form
    }

    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':

        tarefa.concluida = True

        tarefa.save()


        return redirect('home')

@login_required
def deletar_tarefa(request, pk):

    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':

        tarefa.delete()

        return redirect('home')
    
def register(request): 
    # Se a requisição for POST, o usuário enviou o formulário 
    if request.method == 'POST': 
        # Cria uma instância do formulário com os dados enviados 
        form = UserCreationForm(request.POST) 
         
        # Verifica se o formulário é válido (ex: senhas batem, username não existe) 
        if form.is_valid(): 
            user = form.save() # Salva o novo usuário no banco 
            login(request, user) # Faz o login automático do usuário 
            return redirect('home') # Redireciona para a home 
         
        # Se o form NÃO for válido, a execução continua 
        # e o 'form' (agora com as mensagens de erro) 
        # será passado para o template no 'context' abaixo. 
     
    # Se a requisição for GET, o usuário apenas visitou a página 
    else: 
        form = UserCreationForm() # Cria um formulário de cadastro vazio 
     
    # Prepara o contexto e renderiza o template 
    context = {'form': form} 
    return render(request, 'register.html', context) 