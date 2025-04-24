from django.urls import path
from api.views import MonthApiView, SeasonApiView

urlpatterns = [
    path("fetch/monthwise", MonthApiView.as_view(), name="fetch_month"),
    path("fetch/seasonwise", SeasonApiView.as_view(), name="fetch_season")
]