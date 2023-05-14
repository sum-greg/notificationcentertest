from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id',
                  'phone_number',
                  'operator_code',
                  'tag',
                  'timezone',
                  ]
