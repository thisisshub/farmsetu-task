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
        
class RegionDBModel(BaseDbModel):
    region = models.CharField(max_length=30, blank=False, null=True, unique=True)
    
    class Meta:
        verbose_name_plural = "Regions"
        unique_together = ("region",)

    @property
    def region_name(self):
        return self.region

class SeasonDbModel(BaseDbModel):
    season = models.CharField(max_length=5, blank=False, null=True, unique=True)
    
    class Meta:
        verbose_name_plural = "Seasons"
        unique_together = ("season",)

class MonthWiseTempratureDbModel(BaseDbModel):
    month = models.CharField(max_length=5, blank=False, null=True)
    temperature = models.CharField(max_length=6, blank=False, null=True)
    region = models.ForeignKey(RegionDBModel, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=False, null=True)
    
    class Meta:
        verbose_name_plural = "Month Wise Temprature"
        unique_together = ("year", "month", "region",)
    
class SeasonWiseTempratureDbModel(BaseDbModel):
    temperature = models.CharField(max_length=6, blank=False, null=True)
    region = models.ForeignKey(RegionDBModel, on_delete=models.CASCADE)
    season = models.ForeignKey(SeasonDbModel, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=False, null=True)
    
    class Meta:
        verbose_name_plural = "Season Wise Temprature"
        unique_together = ("year", "season", "region",)