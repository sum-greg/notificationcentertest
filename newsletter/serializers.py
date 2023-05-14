from abc import ABC

from rest_framework import serializers

from .models import NewsLetter
from message.serializers import MessageSerializer


class NewsLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsLetter
        fields = ['id',
                  'start_datetime',
                  'end_datetime',
                  'text_message',
                  'client_filter_operator_code',
                  'client_filter_tag',
                  ]


class StatisticSerializer(serializers.Serializer):
    total_messages = serializers.IntegerField()
    sent_messages = serializers.IntegerField()
    failed_messages = serializers.IntegerField()
    messages = MessageSerializer(many=True)
