from rest_framework import serializers
from .models import User, Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['id','title','content','user']

# class BlogSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     user = serializers.CharField()