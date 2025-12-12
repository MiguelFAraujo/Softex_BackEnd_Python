from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    # Mostra o username (read-only) em vez do ID
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'concluida', 'criada_em']
        # Impedir que o cliente envie/edite esses campos
        read_only_fields = ['id', 'user', 'criada_em']