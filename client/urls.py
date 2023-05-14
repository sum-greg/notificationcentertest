from django.urls import path

from .views import ClientCreate, ClientList, ClientDetail, ClientUpdate, ClientDelete


urlpatterns = [
    path('create/', ClientCreate.as_view(), name='create-client'),
    path('', ClientList.as_view(), name='list-clients'),
    path('<int:pk>/', ClientDetail.as_view(), name='retrieve-client'),
    path('update/<int:pk>/', ClientUpdate.as_view(), name='update-client'),
    path('delete/<int:pk>/', ClientDelete.as_view(), name='delete-client'),
]
