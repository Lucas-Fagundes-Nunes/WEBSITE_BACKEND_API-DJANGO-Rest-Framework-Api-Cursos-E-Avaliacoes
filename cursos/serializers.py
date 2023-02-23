from django.db.models import Avg
from rest_framework import serializers

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    def validate_avaliacao(self, valor): # nome função tem que ser validate e campo que quer mexer
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')



class CursoSerializer(serializers.ModelSerializer):
    # Nested Relation ship
        # Linha de baixo é para fazer uma lista dentro do json de avaliações de cada curso
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True) # Many = mais de uma avaliação // read_only = apenas leituras

    # HyperLinked Related Field
        # Disponibiliza o linkdas avaliações
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name= 'avaliacao-detail'
    )
    """

    # Primary Key Related Field
        # Disponibiliza apenas o id das avaliações
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #   Media de avalações 
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0

        return round(media * 2) / 2