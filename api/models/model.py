from uuid import uuid4
from django.db import models
from api.enum import MonthEnum, SeasonEnum, RegionEnum


class BaseDbModel(models.Model):
    record_created_at = models.DateTimeField(auto_now_add=True)
    record_updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid4)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class MonthWiseTempratureDbModel(BaseDbModel):
    region = models.CharField(max_length=30, blank=False, null=True, choices=RegionEnum.choices())
    month = models.CharField(max_length=5, blank=False, null=True, choices=MonthEnum.choices())
    temperature = models.CharField(max_length=6, blank=False, null=True)
    year = models.CharField(max_length=4, blank=False, null=True)
    
    class Meta:
        verbose_name_plural = "Month Wise Temprature"
    
class SeasonWiseTempratureDbModel(BaseDbModel):
    region = models.CharField(max_length=30, blank=False, null=True, choices=RegionEnum.choices())
    season = models.CharField(max_length=5, blank=False, null=True, choices=SeasonEnum.choices())
    temperature = models.CharField(max_length=6, blank=False, null=True)
    year = models.CharField(max_length=4, blank=False, null=True)