from django.urls import path , include
from .views import ProjectsListView, ProjectsDetailView, StatusChoiceChangeAPIView

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='post_projects'),
    path('projects/<int:pk>/', ProjectsDetailView.as_view(), name='get_projects'),
    path('status-choice-change/', StatusChoiceChangeAPIView.as_view(), name='status_choice_change_api'),
    path('status-choice-change/<int:pk>/', StatusChoiceChangeAPIView.as_view(), name='status_choice_change_detail_api'),
]
