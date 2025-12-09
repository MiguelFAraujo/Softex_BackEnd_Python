from django.urls import path
from .views import ListaTarefasAPIView

urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
]