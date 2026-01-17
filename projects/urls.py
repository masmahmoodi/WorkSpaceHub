from django.urls import path
from .views import ProjectListCreateView, ProjectRetriveUpdateDestroy
urlpatterns = [
   path("projects/", ProjectListCreateView.as_view(), name="list_create_projects"),
   path("projects/<int:pk>/",  ProjectRetriveUpdateDestroy.as_view(), name="project_details" )
   
]
