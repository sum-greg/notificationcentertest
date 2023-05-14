from django.urls import path

from .views import (
    NewsLetterCreate, NewsLetterList, NewsLetterDetail, NewsLetterUpdate,
    NewsLetterDelete, StatisticView, SendMessagesView
)

urlpatterns = [
    path('create/', NewsLetterCreate.as_view(), name='create-newsletter'),
    path('', NewsLetterList.as_view(), name='list-newsletters'),
    path('<int:pk>/', NewsLetterDetail.as_view(), name='retrieve-newsletter'),
    path('update/<int:pk>/', NewsLetterUpdate.as_view(), name='update-newsletter'),
    path('delete/<int:pk>/', NewsLetterDelete.as_view(), name='delete-newsletter'),
    path('statistic/<int:pk>/', StatisticView.as_view(), name='statistic'),
    path('send/', SendMessagesView.as_view(), name='send-messages'),
]
