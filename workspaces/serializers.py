from rest_framework import serializers
from .models import Workspace, WorkspaceMember

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'slug', 'plan', 'is_active', 'created_at']

class WorkspaceMemberSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    workspace_name = serializers.ReadOnlyField(source='workspace.name')

    class Meta:
        model = WorkspaceMember
        fields = ['id', 'user', 'user_username', 'workspace', 'workspace_name', 'role']