from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer

class ListaTarefasAPIView(APIView):
    """
    View para listar (GET) e criar (POST) tarefas.
    """
    
    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # --- NOVO MÉTODO POST ---
    def post(self, request, format=None):
        # 1. Instanciar o Serializer com os dados recebidos
        serializer = TarefaSerializer(data=request.data)

        # 2. Verificar se os dados são válidos
        if serializer.is_valid():
            # 3. Salvar no banco
            serializer.save()
            
            # 4. Retornar 201 Created com os dados salvos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 5. Se der erro, retornar 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)