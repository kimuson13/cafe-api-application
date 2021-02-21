from rest_framework import serializers

from core.models import Tag, Cafe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class CafeSerializer(serializers.ModelSerializer):
    """Serializer for Cafe objects"""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Cafe
        fields = [
            'id', 'name', 'tags', 'address',
            'opening_time', 'close_time'
        ]
        read_only_fields = ['id']


class CafeDetailSerializer(CafeSerializer):
    """Serializer a cafe detail"""
    tags = TagSerializer(many=True, read_only=True)
