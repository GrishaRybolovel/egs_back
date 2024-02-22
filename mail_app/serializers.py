from rest_framework import serializers
from .models import Mails


class MailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mails
        fields = '__all__'
