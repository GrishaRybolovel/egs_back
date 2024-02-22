from rest_framework import generics
from .models import Mails
from .serializers import MailsSerializer


class MailsListCreateView(generics.ListCreateAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailsSerializer


class MailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailsSerializer
