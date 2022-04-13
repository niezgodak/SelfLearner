from words.models import Word
from rest_framework import serializers

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class WordEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['counter', 'is_learned']

