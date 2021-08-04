from rest_framework import serializers

from .models import AuthorSubscriber


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorSubscriber
        fields = ['author', 'subscriber']

    def validate(self, attrs):
        if attrs.get('author') == attrs.get('subscriber'):
            raise serializers.ValidationError('There is no way to subscribe to yourself')
        return attrs


class SubscribeStatusSerializer(serializers.Serializer):
    status = serializers.BooleanField()
