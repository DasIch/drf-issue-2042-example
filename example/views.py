from rest_framework.viewsets import ModelViewSet

from example import serializers, models


class A(ModelViewSet):
    queryset = models.A.objects.all()
    serializer_class = serializers.A


class B(ModelViewSet):
    queryset = models.B.objects.all()
    serializer_class = serializers.B