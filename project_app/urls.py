from django.urls import path , include
from .views import ProjectsListView, ProjectsDetailView

urlpatterns = [
    path('projects/', ProjectsListView.as_view(), name='post_projects'),
    path('projects/<int:pk>/', ProjectsDetailView.as_view(), name='get_projects'),
]
