from django.contrib.auth import get_user_model
from  rest_framework import serializers
user = get_user_model()

class MeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user
        fields =("id","username", "email")
        read_only_fields=("id",)

        