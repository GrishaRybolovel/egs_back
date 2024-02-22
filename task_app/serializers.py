from rest_framework import serializers
from .models import Tasks
from user_app.models import CustomUser
from project_app.models import Projects
from user_app.serializers import CustomUserSerializer
from project_app.serializers import ProjectsSerializer


class TasksSerializer(serializers.ModelSerializer):
    task_to_user = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = '__all__'
