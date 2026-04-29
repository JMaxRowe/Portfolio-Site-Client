from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
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
    owner = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        roles_data = validated_data.pop('roles', [])
        
        project = Project.objects.create(**validated_data)
        
        for tag in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(name=tag['name'])
            project.tags.add(tag_obj)
        
        for role in roles_data:
            role_obj, _ = Role.objects.get_or_create(name=role['name'])
            project.roles.add(role_obj)
        
        return project