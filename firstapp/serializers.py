from rest_framework.serializers import ModelSerializer

from firstapp.models import Dishes


class DishesSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = '__all__'
