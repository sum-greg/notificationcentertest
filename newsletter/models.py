from django.db import models
from rest_framework.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver


class NewsLetter(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    text_message = models.TextField()
    client_filter_operator_code = models.CharField(max_length=10)
    client_filter_tag = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - \'{self.text_message}\'...'


@receiver(pre_save, sender=NewsLetter)
def newsletter_pre_save(sender, instance, **kwargs):
    if instance.start_datetime >= instance.end_datetime:
        raise ValidationError("End datetime must be greater than start datetime")
