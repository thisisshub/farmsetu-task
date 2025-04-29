from django.contrib import admin
from .models.model import MonthWiseTempratureDbModel, SeasonWiseTempratureDbModel, RegionDBModel, SeasonDbModel


@admin.register(RegionDBModel)
class RegionDBModelAdmin(admin.ModelAdmin):
    list_display = ('region', 'is_active', 'record_created_at', 'record_updated_at')
    search_fields = ('region',)
    list_filter = ('is_active', 'record_created_at', 'record_updated_at')
    ordering = ('-record_created_at',)

@admin.register(SeasonDbModel)
class SeasonDbModelAdmin(admin.ModelAdmin):
    list_display = ('get_region', 'season', 'is_active', 'record_created_at', 'record_updated_at')
    search_fields = ('season',)
    list_filter = ('is_active', 'record_created_at', 'record_updated_at')
    ordering = ('-record_created_at',)
    
    def get_region(self, obj):
        return obj.region.region

@admin.register(MonthWiseTempratureDbModel)
class MonthWiseTempratureDbModelAdmin(admin.ModelAdmin):
    list_display = ('get_region', 'month', 'temperature', 'year', 'is_active', 'record_created_at')
    search_fields = ('region__region', 'month', 'temperature', 'year')
    list_filter = ('region', 'month', 'is_active', 'year', 'record_created_at')
    ordering = ('-record_created_at',)
    raw_id_fields = ('region',)

    def get_region(self, obj):
        return obj.region.region

@admin.register(SeasonWiseTempratureDbModel)
class SeasonWiseTempratureDbModelAdmin(admin.ModelAdmin):
    list_display = ('region', 'season', 'temperature', 'year', 'is_active', 'record_created_at')
    search_fields = ('region__region', 'season__season', 'temperature', 'year')
    list_filter = ('region', 'season', 'is_active', 'year', 'record_created_at')
    ordering = ('-record_created_at',)
    raw_id_fields = ('region', 'season')

