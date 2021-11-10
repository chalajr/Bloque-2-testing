from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from accounts.models import UserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data["password"]
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
