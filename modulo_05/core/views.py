from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Tarefa
from .serializers import TarefaSerializer, UserRegistrationSerializer
from .permissions import IsGerente

# --- NOVAS VIEWS DA APOSTILA 5 ---

class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (AllowAny).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer


# --- VIEWS EXISTENTES (ATUALIZADAS) ---

class ListaTarefasAPIView(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # RLS: Retorna apenas tarefas do usuário logado
        return Tarefa.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Vincula a tarefa criada ao usuário atual
        serializer.save(user=self.request.user)


class DetalheTarefaAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer
    # Removemos 'permission_classes' fixo para usar o método dinâmico abaixo

    def get_queryset(self):
        # RLS: Garante que só acessa/edita/deleta se for dono
        return Tarefa.objects.filter(user=self.request.user)

    def get_permissions(self):
        """
        Define a permissão baseada na ação (RBAC):
        - DELETE: Exige autenticação E grupo 'Gerente'.
        - OUTROS: Exige apenas autenticação (e ser dono).
        """
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), IsGerente()]
        
        return [IsAuthenticated()]


# --- VIEWS UTILITÁRIAS ---

class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            f"Usuário autenticado: {request.user.username}", 
            status=status.HTTP_200_OK
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"detail": "Logout realizado com sucesso."}, 
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"detail": "Token inválido."}, 
                status=status.HTTP_400_BAD_REQUEST
            )