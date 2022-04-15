from words.models import Word, WordGroup
from rest_framework import serializers

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class WordEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['counter', 'is_learned']

class WordGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordGroup
        fields = '__all__'