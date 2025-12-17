from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id', 'user', 'criada_em']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """
        Intercepta a criação para usar o 'create_user' e hashear a senha.
        E adiciona o usuário ao grupo 'Comum'.
        """
        # 1. Cria o usuário (Lógica do Cap. 3)
        password = validated_data.pop('password')
        email = validated_data.get('email', '')
        username = validated_data['username']
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # 2. Lógica de Atribuição de Cargo (Role) 
        try: 
            # Busca o grupo 'Comum' 
            grupo_comum = Group.objects.get(name='Comum') 
            # Adiciona o usuário ao grupo 
            user.groups.add(grupo_comum) 
        except Group.DoesNotExist: 
            # Fallback: Se o grupo não existir, o usuário é criado sem grupo. 
            # Em produção, deveríamos logar um erro aqui. 
            pass
            
        return user