from .serializers import ProjectSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Project
from rest_framework.permissions import IsAuthenticated
#  projects list and create view
class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    #  create a project 
    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)


class ProjectRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    # show data to authorized users
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    

