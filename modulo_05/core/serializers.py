from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Tarefa

# Serializer de Tarefas (Apostila 4 + 5)
class TarefaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # Apenas leitura na saída [8]

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id', 'user', 'criada_em']

# Novo Serializer de Registro (Apostila 5)
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    ) # write_only garante que a senha não retorne no JSON [6]

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        # Cria usuário com hash de senha seguro [6]
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=password
        )
        # Atribuição automática ao grupo 'Comum' [7]
        try:
            grupo_comum = Group.objects.get(name='Comum')
            user.groups.add(grupo_comum)
        except Group.DoesNotExist:
            pass
        return user