from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        # Removemos 'user' temporariamente da obrigatoriedade
        fields = ['id', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id', 'criada_em']

    # Validação Customizada
    def validate_titulo(self, value):
        # Remover espaços em branco no início e fim
        value = value.strip()

        # Regra 1: Não pode ser vazio
        if not value:
            raise serializers.ValidationError("O título não pode ser vazio.")

        # Regra 2: Mínimo de 3 caracteres
        if len(value) < 3:
            raise serializers.ValidationError("O título deve ter pelo menos 3 caracteres.")
            
        # Regra 3: Não pode ser só números
        if value.isdigit():
             raise serializers.ValidationError("O título não pode conter apenas números.")

        return value