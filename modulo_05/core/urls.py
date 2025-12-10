<<<<<<< HEAD
from django.urls import path
from .views import ListaTarefasAPIView

urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
=======
from .views import ListaTarefasAPIView, DetalheTarefaAPIView
from django.urls import path

app_name = 'core'

urlpatterns = [
    # Rota antiga (Coleção)
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    
    # O <int:pk> é o que captura o número da URL (ex: 1, 42)
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
>>>>>>> feat/m5/gabarito/ap_03
]