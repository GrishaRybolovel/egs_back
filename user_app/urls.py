from django.urls import path , include
from .views import RegisterView, LoginApi, UserProfileView, ListUsersView, UserRetrieveUpdateDestroyView, CreateUserView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('users/', ListUsersView.as_view(), name='users'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('user-create/', CreateUserView.as_view(), name='user-create'),
]
