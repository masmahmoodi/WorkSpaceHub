from .serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView
from .models import Project
from rest_framework.permissions import IsAuthenticated

class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)