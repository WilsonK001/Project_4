from django.urls import path
from . import views


urlpatterns = [
    #  api/contacts will be routed to the dogList view for handling
    path('api/dogs', views.DogList.as_view(), name='dog_list'),

    # api/contacts will be routed to the dogDetail view for handling
    path('api/dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'),
]

