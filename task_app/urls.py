from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, FileDownloadView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('tasks/download/<str:file_path>/', FileDownloadView.as_view(), name='file_download'),
]
