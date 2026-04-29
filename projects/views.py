from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers.common import ProjectSerializer
from rest_framework import permissions
from rest_framework.exceptions import NotFound



class ProjectListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serialized_projects = ProjectSerializer(projects, many=True)
        return Response(serialized_projects.data)
    
    def post(self, request):
        serialized_project = ProjectSerializer(data=request.data)
        serialized_project.is_valid(raise_exception=True)
        serialized_project.save(owner=request.user)
        return Response(serialized_project.data, status=201)
    

    
class ProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_project(self, slug):
        try:
            return Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            raise NotFound('Project not found.')
        
    def get(self, request, slug):
        project = self.get_project(slug)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)
    
    def patch(self, request, slug):
        project = self.get_project(slug)
        serialized_project = ProjectSerializer(project, data=request.data, partial=True)
        serialized_project.is_valid(raise_exception=True)
        serialized_project.save()
        return Response(serialized_project.data)
    
    def delete(self, request, slug):
        project = self.get_project(slug)
        project.delete()
        return Response(status=204)