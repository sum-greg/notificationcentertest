from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer


class MessageCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Message
    queryset = Message.objects.all(),
    serializer_class = MessageSerializer


class MessageList(generics.ListAPIView):
    # API endpoint that allows Messages to be viewed
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Message by id
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Message record to be updated
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Message record to be deleted
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
