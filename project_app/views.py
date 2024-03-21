from user_app.models import CustomUser
from .models import Projects, StatusChoiceChange
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import ProjectsSerializer, StatusChoiceChangeSerializer
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from rest_framework import status


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


class StatusChoiceChangeAPIView(APIView):
    def get(self, request, project_id):
        try:
            status_changes = StatusChoiceChange.objects.filter(project_id=project_id)
            serializer = StatusChoiceChangeSerializer(status_changes, many=True)
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        except StatusChoiceChange.DoesNotExist:
            raise NotFound(detail="Project not found")

    def post(self, request):
        serializer = StatusChoiceChangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        status_change = self.get_object(pk)
        serializer = StatusChoiceChangeSerializer(status_change, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        status_change = self.get_object(pk)
        status_change.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
