from django.urls import path
from .views import MailsListCreateView, MailsRetrieveUpdateDestroyView

urlpatterns = [
    path('mails/', MailsListCreateView.as_view(), name='mails-list-create'),
    path('mails/<int:pk>/', MailsRetrieveUpdateDestroyView.as_view(), name='mails-retrieve-update-destroy'),
]
