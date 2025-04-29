from api.enum import MonthEnum, RegionEnum, SeasonEnum
from rest_framework.serializers import ModelSerializer
from api.models import (
    SeasonWiseTempratureDbModel,
    MonthWiseTempratureDbModel,
    RegionDBModel,
)


class MonthWiseTempratureSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MonthWiseTempratureDbModel

    def validate_region(self, attrs):
        region_choices = {i.region: str(i.id) for i in RegionDBModel.objects.all()}
        if self.initial_data["region"] in region_choices:
            self.initial_data["region"] = region_choices[self.initial_data["region"]]
        return super().validate(attrs)


class SeasonWiseTempratureSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SeasonWiseTempratureDbModel

    def validate_region(self, attrs):
        region_choices = {i.region: str(i.id) for i in RegionDBModel.objects.all()}
        if self.initial_data["region"] in region_choices:
            self.initial_data["region"] = region_choices[self.initial_data["region"]]
        return super().validate(attrs)
