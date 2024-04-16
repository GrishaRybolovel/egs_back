from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    email = serializers.CharField()
    name = serializers.CharField()
    surname = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        # fields = ('id', 'email', 'name', 'surname', 'last_name', 'password')
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def create(self, validated_data):
        id = validated_data.pop('id', None)
        password = validated_data.pop('password')

        if id is not None:
            # Check if an object with the provided ID already exists
            instance, created = CustomUser.objects.update_or_create(id=id, defaults=validated_data)
        else:
            # If ID is not provided, create a new object using the default create method
            instance = CustomUser.objects.create(**validated_data)

        instance.set_password(password)
        instance.save()
        return instance