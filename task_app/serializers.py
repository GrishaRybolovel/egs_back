from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = '__all__'

    def get_type(self, obj):
        if obj.project:
            return obj.project.proj_type if hasattr(obj.project, 'proj_type') else None
        else:
            return None
