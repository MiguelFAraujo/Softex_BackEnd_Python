from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Tarefa
from .serializers import TarefaSerializer

# Lista tarefas e permite criação (POST injeta usuário automaticamente)
class TarefaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # Proteção [cite: 136]

    # MÉTODO CHAVE: Injeta o usuário logado antes de salvar [cite: 137]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Detalhes, atualização e exclusão de UMA tarefa
class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # Proteção [cite: 151]

# View de Logout (Blacklist)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist() # Adiciona o token à lista negra [cite: 287]
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"detail": "Token inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )