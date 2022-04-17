import django
from django.core.validators import MinLengthValidator
from django.db import models


class Inquiry(models.Model):
    name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=10, blank=True, null=True, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=254)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)


class Otp(models.Model):
    mobile_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    otp = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
