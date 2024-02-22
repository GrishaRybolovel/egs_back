from django.urls import path
from .views import MessageListCreateView, MessageRetrieveUpdateDestroyView, FileDownloadView

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='task-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('messages/download/<str:file_path>/', FileDownloadView.as_view(), name='file_download'),
]
