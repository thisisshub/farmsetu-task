from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from api.models import MonthWiseTempratureDbModel, SeasonWiseTempratureDbModel
from api.serializer import SeasonWiseTempratureSerializer, MonthWiseTempratureSerializer


class MonthApiView(generics.ListAPIView, LimitOffsetPagination):
    filter_backends = [DjangoFilterBackend]
    serializer_class = MonthWiseTempratureSerializer
    queryset = MonthWiseTempratureDbModel.objects.all()
    filterset_fields = ("month", "region", "year", "temperature",)


class SeasonApiView(generics.ListAPIView, LimitOffsetPagination):
    filter_backends = [DjangoFilterBackend]
    serializer_class = SeasonWiseTempratureSerializer
    queryset = SeasonWiseTempratureDbModel.objects.all()
    filterset_fields = ("season", "region", "year", "temperature",)

