from django.urls import path , include
from .views import RegisterView, LoginApi, UserProfileView, ListUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('users/', ListUsersView.as_view(), name='users'),
]
