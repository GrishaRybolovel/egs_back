from django.shortcuts import render
from rest_framework import generics
from .models import Projects
from user_app.models import CustomUser
from .serializers import ProjectsSerializer
from rest_framework.response import Response


class ProjectsListView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context.update({
    #         'json_dumps_params': {'ensure_ascii': False, 'indent': 2}  # Add your custom parameters
    #     })
    #     return context


class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context.update({
    #         'json_dumps_params': {'ensure_ascii': False, 'indent': 2}  # Add your custom parameters
    #     })
    #     return context

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Manually update project_to_user relationship
        project_to_user_data = request.data.pop('project_to_user', [])
        if project_to_user_data != []:
            instance.project_to_user.clear()
            for user_data in project_to_user_data:
                user_id = user_data.get('id')
                if user_id:
                    user = CustomUser.objects.get(id=user_id)
                    instance.project_to_user.add(user)

        # Call the update method of the serializer to update other fields
        serializer.update(instance, request.data)

        return Response(serializer.data)
