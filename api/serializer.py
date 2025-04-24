from rest_framework.serializers import ModelSerializer
from api.models import SeasonWiseTempratureDbModel, MonthWiseTempratureDbModel


class MonthWiseTempratureSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MonthWiseTempratureDbModel


class SeasonWiseTempratureSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SeasonWiseTempratureDbModel
