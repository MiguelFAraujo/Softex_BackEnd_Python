from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tarefa

class SecurityTests(TestCase):
    def setUp(self):
        # 1. Configurar Grupos (Dependência vital da Apostila 5)
        self.grupo_comum = Group.objects.create(name='Comum')
        self.grupo_gerente = Group.objects.create(name='Gerente')

        # 2. Criar Usuários
        self.user_comum = User.objects.create_user(username='funcionario', password='123')
        # Usuário comum entra no grupo automaticamente pelo Serializer no cadastro, 
        # mas aqui criamos manualmente para testar as permissões isoladas.
        self.user_comum.groups.add(self.grupo_comum)

        self.user_gerente = User.objects.create_user(username='chefe', password='123')
        self.user_gerente.groups.add(self.grupo_gerente)
        
        self.user_hacker = User.objects.create_user(username='hacker', password='123')
        self.user_hacker.groups.add(self.grupo_comum)

        # 3. Criar Tarefa do Funcionário
        self.tarefa = Tarefa.objects.create(
            user=self.user_comum, 
            titulo="Relatório Mensal"
        )

        # Cliente de teste
        self.client = APIClient()

    # --- TESTE 1: Cadastro Automático de Grupo ---
    def test_registro_atribui_grupo_comum(self):
        """Teste se novos usuários ganham o grupo 'Comum' automaticamente [cite: 576-579]"""
        data = {
            "username": "novato",
            "email": "novato@teste.com",
            "password": "senha_segura"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        user_novo = User.objects.get(username="novato")
        self.assertTrue(user_novo.groups.filter(name='Comum').exists(), "Usuário deveria estar no grupo Comum")

    # --- TESTE 2: Row Level Security (Isolamento) ---
    def test_rls_usuario_nao_ve_tarefa_alheia(self):
        """Hacker não pode ver a tarefa do funcionário [cite: 580-585]"""
        self.client.force_authenticate(user=self.user_hacker)
        
        # Tenta listar (deve vir vazio)
        response_list = self.client.get('/api/tarefas/')
        self.assertEqual(len(response_list.data), 0)

        # Tenta acessar ID direto (deve ser 404, não 403 - Segurança por Omissão)
        response_detail = self.client.get(f'/api/tarefas/{self.tarefa.id}/')
        self.assertEqual(response_detail.status_code, status.HTTP_404_NOT_FOUND)

    # --- TESTE 3: RBAC (Bloqueio de Delete) ---
    def test_comum_nao_pode_deletar(self):
        """Funcionário (Dono) tenta deletar, mas não é Gerente -> 403 Forbidden [cite: 586-591]"""
        self.client.force_authenticate(user=self.user_comum)
        
        response = self.client.delete(f'/api/tarefas/{self.tarefa.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- TESTE 4: RBAC (Sucesso de Delete) ---
    def test_gerente_pode_deletar(self):
        """Gerente tenta deletar -> Precisa primeiro ter acesso via RLS, depois permissão"""
        # IMPORTANTE: Na nossa regra atual, o Gerente precisa SER DONO da tarefa para vê-la (RLS),
        # E ser GERENTE para deletá-la (RBAC).
        
        # 1. Gerente cria sua própria tarefa
        tarefa_gerente = Tarefa.objects.create(user=self.user_gerente, titulo="Demitir alguém")
        
        self.client.force_authenticate(user=self.user_gerente)
        
        response = self.client.delete(f'/api/tarefas/{tarefa_gerente.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)