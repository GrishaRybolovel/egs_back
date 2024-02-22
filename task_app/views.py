from rest_framework import generics, permissions
from .models import Tasks
from .serializers import TasksSerializer
from user_app.models import CustomUser
from rest_framework.response import Response
from project_app.models import Projects


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        request_data = self.request.data

        task_to_user_data = request_data.pop('task_to_user', [])
        task_to_user_array = []
        if task_to_user_data != []:
            for user_data in task_to_user_data:
                user_id = user_data.get('id')
                if user_id:
                    user = CustomUser.objects.get(id=user_id)
                    task_to_user_array.append(user)
        serializer.validated_data['task_to_user'] = task_to_user_array

        serializer.save()


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Manually update project_to_user relationship
        task_to_user_data = request.data.pop('task_to_user', [])

        author_id = request.data.pop('author', None)
        project_id = request.data.pop('project', None)

        if author_id:
            author = CustomUser.objects.get(id=author_id)
            instance.author = author

        if project_id:
            project = Projects.objects.get(id=project_id)
            instance.project = project


        if task_to_user_data != []:
            instance.task_to_user.clear()
            for user_data in task_to_user_data:
                user_id = user_data.get('id')
                if user_id:
                    user = CustomUser.objects.get(id=user_id)
                    instance.task_to_user.add(user)

        # Call the update method of the serializer to update other fields
        serializer.update(instance, request.data)

        return Response(serializer.data)
