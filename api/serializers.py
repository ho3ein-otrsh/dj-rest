from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from account.models import User
from blog.models import Article

class ArticleSerializer(ModelSerializer):

    username = serializers.CharField(source="author.username", read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

        
    def validate_author(self, value):
        user = self.context['request'].user
        if  user == value or user.is_superuser : 
            return value
        raise serializers.ValidationError("author is invalid")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'