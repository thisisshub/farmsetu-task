import os
import json
import requests
import tempfile
import pandas as pd
from celery import shared_task
from api.enum import RegionEnum, ParameterEnum, SeasonEnum, MonthEnum
from api.serializer import SeasonWiseTempratureSerializer, MonthWiseTempratureSerializer


@shared_task
def update_tempratures():
    for region in RegionEnum:
        for parameter in ParameterEnum:
            url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter.value}/date/{region.value}.txt"
            data = requests.get(url=url).text

            with tempfile.NamedTemporaryFile(
                mode="w", delete=False, suffix=".txt"
            ) as temp_file:
                temp_file.write(data)
                temp_file_path = temp_file.name

            try:
                df = pd.read_csv(temp_file_path, sep="\s+", skiprows=5)
                data = df.to_json(orient="records", lines=False)

                result_month = [
                    {
                        "region": region.value,
                        "year": record["year"],
                        "month": month,
                        "temperature": temperature,
                    }
                    for record in json.loads(data)
                    for month, temperature in record.items()
                    if month not in [i.value for i in SeasonEnum] + ["year"]
                ]

                result_season = [
                    {
                        "region": region.value,
                        "year": record["year"],
                        "season": season,
                        "temperature": temperature,
                    }
                    for record in json.loads(data)
                    for season, temperature in record.items()
                    if season not in [i.value for i in MonthEnum] + ["year"]
                ]

                serializer_month = MonthWiseTempratureSerializer(
                    data=result_month, many=True
                )
                serializer_month.is_valid(raise_exception=True)
                serializer_month.save()

                serializer_season = SeasonWiseTempratureSerializer(
                    data=result_season, many=True
                )
                serializer_season.is_valid(raise_exception=True)
                serializer_season.save()

            finally:
                os.unlink(temp_file_path)
