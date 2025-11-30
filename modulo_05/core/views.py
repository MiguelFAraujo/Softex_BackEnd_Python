from rest_framework.views import APIView 
from rest_framework.response import Response 
from .models import Tarefa 
from .serializers import TarefaSerializer 

class ListaTarefasAPIView(APIView): 

 
# Este método é chamado quando a requisição HTTP é GET 
    def get(self, request, format=None): 
        # 1. ORM: Busca todos os objetos do Model 
        tarefas = Tarefa.objects.all() 
        # 2. Serializa os objetos, indicando 'many=True' para a lista 
        serializer = TarefaSerializer(tarefas, many=True) 
        # 3. Retorna os dados serializados como JSON 
        return Response(serializer.data)