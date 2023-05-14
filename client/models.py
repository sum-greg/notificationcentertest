from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_regex = RegexValidator(regex=r'^7\d{10}$', message="Номер телефона должен быть в формате 7XXXXXXXXXX")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number
