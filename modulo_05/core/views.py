from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.shortcuts import get_object_or_404

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
class DetalheTarefaAPIView(APIView):
    """
    View para operações em UMA tarefa específica:
    - GET: Visualizar
    - PUT: Atualizar tudo
    - PATCH: Atualizar parcial
    - DELETE: Apagar
    """

    # Método auxiliar para buscar a tarefa ou dar erro 404
    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    # 1. GET - Buscar uma tarefa específica
    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa) # Sem many=True, pois é um só
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. PUT - Atualizar TUDO (Exige todos os campos)
    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. PATCH - Atualizar PARCIAL (Ex: só marcar como concluída)
    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        
        # O segredo do PATCH é o partial=True
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. DELETE - Apagar a tarefa
    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        # Retorna 204 (Sucesso sem conteúdo)
        return Response(status=status.HTTP_204_NO_CONTENT)