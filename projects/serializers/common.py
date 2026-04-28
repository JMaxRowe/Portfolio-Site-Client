from rest_framework.serializers import ModelSerializer
from ..models import Project, Tag, Role

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    roles = RoleSerializer(many=True)
    
    class Meta:
        model = Project
        fields = '__all__'