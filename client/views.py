from rest_framework import generics

from .models import Client
from .serializers import ClientSerializer


class ClientCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Client
    queryset = Client.objects.all(),
    serializer_class = ClientSerializer


class ClientList(generics.ListAPIView):
    # API endpoint that allows Clients to be viewed
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Client by id
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Client record to be updated
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Client record to be deleted
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
