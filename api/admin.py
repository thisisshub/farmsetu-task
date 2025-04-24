from django.contrib import admin
from .models.model import MonthWiseTempratureDbModel, SeasonWiseTempratureDbModel


@admin.register(MonthWiseTempratureDbModel)
class MonthWiseTempratureDbModelAdmin(admin.ModelAdmin):
    list_display = ('region', 'month', 'temperature', 'year', 'is_active', 'record_created_at')
    search_fields = ('region', 'month', 'temperature',)
    list_filter = ('region', 'month', 'is_active', 'year', 'record_created_at')
    ordering = ('-record_created_at',)

@admin.register(SeasonWiseTempratureDbModel)
class SeasonWiseTempratureDbModelAdmin(admin.ModelAdmin):
    list_display = ('region', 'season', 'temperature', 'year', 'is_active', 'record_created_at')
    search_fields = ('region', 'season', 'temperature',)
    list_filter = ('region', 'season', 'is_active', 'year', 'record_created_at')
    ordering = ('-record_created_at',)
