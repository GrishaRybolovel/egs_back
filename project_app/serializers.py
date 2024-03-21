from rest_framework import serializers
from .models import Projects, StatusChoiceChange
from user_app.serializers import CustomUserSerializer


class ProjectsSerializer(serializers.ModelSerializer):
    project_to_user = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'

class StatusChoiceChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusChoiceChange
        fields = '__all__'
