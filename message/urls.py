from django.urls import path

from .views import MessageCreate, MessageList, MessageDetail, MessageUpdate, MessageDelete


urlpatterns = [
    path('create/', MessageCreate.as_view(), name='create-message'),
    path('', MessageList.as_view(), name='list-messages'),
    path('<int:pk>/', MessageDetail.as_view(), name='retrieve-message'),
    path('update/<int:pk>/', MessageUpdate.as_view(), name='update-message'),
    path('delete/<int:pk>/', MessageDelete.as_view(), name='delete-message'),
]
