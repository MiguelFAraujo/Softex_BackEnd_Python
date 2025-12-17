from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Tarefa
from .serializers import TarefaSerializer, UserRegistrationSerializer
from .permissions import IsGerente

# --- CADASTRO (Apostila 5) ---

class RegisterView(generics.CreateAPIView): 
    """ 
    Endpoint para cadastro de novos usuários. 
    Acesso: Público (Qualquer um pode criar conta). 
    """ 
    queryset = User.objects.all() 
    permission_classes = [AllowAny] # Sobrescreve o padrão global 
    serializer_class = UserRegistrationSerializer 

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    """
    Substitui a antiga ListaTarefasAPIView.
    Agora deixa claro que LISTA e CRIA.
    """
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        """ 
        Sobrescreve o comportamento padrão para retornar APENAS 
        os dados pertencentes ao usuário logado. 
        """ 
        # 1. Recupera o usuário validado pelo JWT 
        user = self.request.user 
        # 2. Retorna o filtro. O Django fará o WHERE user_id = X no banco. 
        return Tarefa.objects.filter(user=user) 

    def perform_create(self, serializer): 
        # Garante que a tarefa criada seja vinculada ao usuário logado 
        serializer.save(user=self.request.user) 


class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = TarefaSerializer  
    def get_queryset(self): 
        return Tarefa.objects.filter(user=self.request.user)  

    def get_permissions(self): 
        """ 
        Instancia e retorna a lista de permissões que esta view requer, 
        dependendo do método HTTP da requisição. 
        """ 
        if self.request.method == 'DELETE': 
            # Para deletar: Precisa estar logado E ser Gerente 
            # A ordem importa: primeiro checa login, depois o grupo 
            return [IsAuthenticated(), IsGerente()] 
        # Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset) 
        return [IsAuthenticated()] 


# --- UTILITÁRIOS (Logout/Testes) ---

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout realizado."}, status=205)
        except Exception:
            return Response({"detail": "Token inválido."}, status=400)