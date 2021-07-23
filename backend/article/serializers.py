from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


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