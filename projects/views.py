from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers.common import ProjectSerializer


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serialized_projects = ProjectSerializer(projects, many=True)
        return Response(serialized_projects.data)