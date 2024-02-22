from django.urls import path
from .views import DocumentsListCreateView, DocumentsRetrieveUpdateDestroyView, FileDownloadView

urlpatterns = [
    path('documents/', DocumentsListCreateView.as_view(), name='documents-list-create'),
    path('documents/<int:pk>/', DocumentsRetrieveUpdateDestroyView.as_view(), name='documents-retrieve-update-destroy'),
    path('documents/download/<str:file_path>/', FileDownloadView.as_view(), name='file_download'),
]