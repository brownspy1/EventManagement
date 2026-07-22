from django.urls import path
from event.views import home,add,update

urlpatterns = [
    path('home/',home,name='home'),
    path('add/<str:id>/',add,name="add"),
    path('update/<str:category>/<int:id>/',update,name="update")
]
