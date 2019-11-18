from rest_framework import serializers
from core.models import Author, Article

# class ArticleSerializer(serializers.Serializer):
#     titulo = serializers.CharField(max_length=120)
#     descripcion = serializers.CharField()
#     cuerpo = serializers.CharField()
#     author_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'nombre', 'email')

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'titulo', 'descripcion', 'cuerpo', 'autor')

