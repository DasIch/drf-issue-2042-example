from rest_framework.serializers import ModelSerializer

from example import models


class A(ModelSerializer):
    class Meta:
        model = models.A


class B(ModelSerializer):
    class Meta:
        model = models.B