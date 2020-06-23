from rest_framework import serializers

from .models import Subdivision, Emploe


class DetailEmploeSerializer(serializers.ModelSerializer):
    position =  serializers.SlugRelatedField(slug_field="title", read_only=True)
    subdivision = serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = Emploe
        fields = ('id', 'name', 'subdivision', 'position', 'date_of_birth', 'photo')


class ListEmploeSerializer(serializers.ModelSerializer):
    position =  serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = Emploe
        fields = ('id', 'name', 'position', 'date_of_birth', 'photo')


class ListSubdivisionSerializer(serializers.ModelSerializer):
    supervisor = ListEmploeSerializer()
    class Meta:
        model = Subdivision
        fields = ('id', 'title', 'supervisor')
