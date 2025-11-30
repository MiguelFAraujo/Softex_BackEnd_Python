from django.urls import path 
from . import views 

urlpatterns = [ 
# Mapeia a URL 'tarefas/' para a View de Classe, usando .as_view() 
    path('tarefas/', views.ListaTarefasAPIView.as_view(), name='lista-tarefas'), 
    ] 