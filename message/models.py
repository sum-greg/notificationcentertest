from django.db import models

from newsletter.models import NewsLetter
from client.models import Client


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    news_letter = models.ForeignKey(NewsLetter, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'\'{self.news_letter.id}\' to \'{self.client.id}\' with status \'{self.status}\''
