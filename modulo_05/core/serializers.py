from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView # Ainda precisa para Logout e MinhaView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarefa
from .serializers import TarefaSerializer


class ListaTarefasAPIView(generics.ListCreateAPIView):
    """
    ListCreateAPIView já faz automaticamente:
    - GET: Lista todas as tarefas (queryset)
    - POST: Cria uma nova tarefa com validação
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    # Opcional: Se quiser manter o comportamento de salvar o usuário logado automaticamente
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetalheTarefaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView já faz automaticamente:
    - GET: Busca uma tarefa pelo ID (pk)
    - PUT/PATCH: Atualiza a tarefa
    - DELETE: Remove a tarefa
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
         return Response(f"Usuário autenticado: {request.user.username}", 
                         status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Token inválido."}, status=status.HTTP_400_BAD_REQUEST)