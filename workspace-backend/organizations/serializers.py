from rest_framework import serializers
from .models import Organization
class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("name","slug",)
        
    def validate_slug(self,value):
            if Organization.objects.filter(slug=value).exists():
                raise serializers.ValidationError("This slug is already in use.")
            return value


class OrganizationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        
        fields = ("id", "name", "slug", "created_at", "updated_at")
        read_only_fields = fields