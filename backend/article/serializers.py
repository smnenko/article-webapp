from rest_framework import serializers

from .models import Article
from authapp.models import User


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Article
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('author').username:
            return super().validate(attrs)
        raise serializers.ValidationError('Before you can create articles, specify a username')


class ArticleTrendingSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'date_created')


class ArticleLatestSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'content', 'topics', 'date_created')
        depth = 1

    def get_content(self, article):
        return article.content[:200].replace('\r', '').replace('\n', ' ')[:100] + '...'