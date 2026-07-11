from django.urls import path
from event.views import home

urlpatterns = [
    path('home/',home,name='home')
]
