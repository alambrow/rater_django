from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from models import Category

class CategoryView(ViewSet):

    def list(self, request):
        """Handle GET for all categories
        """
        categories = Category.objects.all()

        serializer = CategorySerializer(
            categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1