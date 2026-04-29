from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers.common import ProjectSerializer
from rest_framework import permissions


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