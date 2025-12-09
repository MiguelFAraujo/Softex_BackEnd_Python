from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id', 'criada_em']

    # Validação customizada ensinada na Apostila 2
    def validate_titulo(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("O título não pode ser vazio.")
        if len(value) < 3:
            raise serializers.ValidationError("O título deve ter pelo menos 3 caracteres.")
        return value