from django.urls import path

from .views import MediaLook

app_name = 'foreignapi'

urlpatterns = [
    path('', MediaLook.as_view(), name='medialook')
]
