from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from ..models import Project, Tag, Role

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []}
        }

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []}
        }

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
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        roles_data = validated_data.pop('roles', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tags_data is not None:
            instance.tags.clear()
            for tag in tags_data:
                tag_obj, _ = Tag.objects.get_or_create(name=tag['name'])
                instance.tags.add(tag_obj)

        if roles_data is not None:
            instance.roles.clear()
            for role in roles_data:
                role_obj, _ = Role.objects.get_or_create(name=role['name'])
                instance.roles.add(role_obj)

        return instance