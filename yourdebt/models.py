from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class OpenDebt(models.Model):
    debt_name = models.CharField(max_length=150)
    amount_owed = models.IntegerField()
    int_rate = models.IntegerField()
    min_payment = models.IntegerField()
    extra_principal = models.IntegerField()
    time_topay = models.IntegerField()
    def _str_(self):
        return self.debt_name


class Mortgage(models.Model):
    mortgage_name = models.CharField(max_length=150)
    purchase_price = models.IntegerField()
    down_payment = models.IntegerField()
    mortgage_term = models.IntegerField()
    int_rate = models.IntegerField()
    property_tax = models.IntegerField()
    property_insurance = models.IntegerField()
    PMI = models.IntegerField()
    first_month = models.IntegerField()
    first_year = models.IntegerField()

    def _str_(self):
        return self.mortgage_name

class CloseDebt(models.Model):
    debt_name = models.CharField(max_length=150)
    amount_owed = models.IntegerField()
    int_rate = models.IntegerField()
    min_payment = models.IntegerField()
    extra_principal = models.IntegerField()
    time_topay = models.IntegerField()
    term = models.IntegerField()


    def _str_(self):
        return self.debt_name
