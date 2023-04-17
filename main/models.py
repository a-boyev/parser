from django.db import models
import datetime

class Entry(models.Model):
    company = models.CharField(max_length=200)
    date = models.IntegerField(default=datetime.datetime.today().day)
    qliq_factual_1 = models.IntegerField(default=0)
    qliq_factual_2 = models.IntegerField(default=0)
    qoil_factual_1 = models.IntegerField(default=0)
    qoil_factual_2 = models.IntegerField(default=0)
    qliq_forecast_1 = models.IntegerField(default=0)
    qliq_forecast_2 = models.IntegerField(default=0)
    qoil_forecast_1 = models.IntegerField(default=0)
    qoil_forecast_2 = models.IntegerField(default=0)
