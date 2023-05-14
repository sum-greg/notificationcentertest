import requests
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewsLetter
from .serializers import NewsLetterSerializer, StatisticSerializer
from message.models import Message
from client.models import Client


class NewsLetterCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new NewsLetter
    queryset = NewsLetter.objects.all(),
    serializer_class = NewsLetterSerializer


class NewsLetterList(generics.ListAPIView):
    # API endpoint that allows NewsLetters to be viewed
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single NewsLetter by id
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a NewsLetter record to be updated
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a NewsLetter record to be deleted
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class StatisticView(generics.ListAPIView):
    # API endpoint that returns a statistic
    serializer_class = StatisticSerializer
    queryset = NewsLetter.objects.all()

    def get(self, request, *args, **kwargs):
        newsletter = self.get_object()
        messages = Message.objects.filter(news_letter=newsletter)
        total_messages = messages.count()
        sent_messages = messages.filter(status='SENT').count()
        failed_messages = messages.filter(status='FAILED').count()

        data = {
            'total_messages': total_messages,
            'sent_messages': sent_messages,
            'failed_messages': failed_messages,
            'messages': messages
        }
        serializer = self.serializer_class(data)

        return Response(serializer.data)


class SendMessagesView(APIView):
    def post(self, request, format=None):
        # Получение списка активных рассылок
        active_newsletters = NewsLetter.objects.filter(start_datetime__lt=timezone.now(), end_datetime__gt=timezone.now())

        for newsletter in active_newsletters:
            # Получение списка клиентов для рассылки
            clients = Client.objects.filter(
                operator_code=newsletter.client_filter_operator_code,
                tag=newsletter.client_filter_tag
            )

            # Отправка сообщения каждому клиенту
            for client in clients:
                # Отправка сообщения клиенту
                response = requests.post(
                    url=f'https://probe.fbrq.cloud/v1/send/{newsletter.id}',
                    data={
                        "id": newsletter.id,
                        "phone": int(client.phone_number),
                        "text": newsletter.text_message
                    },
                    headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTUyNzMxMDEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkdyZWdvcnkgU3VtbGluc2t5In0.otAlRGXR_lZbYaUrUgf5XXWz-dyph4EK5bwu5Rufczc'}
                )
                response_status = 'SENT'
                if response.status_code == 400:
                    response_status = 'FAILED'

                # Сохранение данных о попытке отправки сообщения клиенту
                message = Message(
                    status=response_status,
                    news_letter=newsletter,
                    client=client
                )
                message.save()

        return Response({'success': True}, status=status.HTTP_200_OK)
