from django.urls import path
from event.views import home,add,update,delete

urlpatterns = [
    path('Dashboard',home,name='home'),
    path('add/<str:id>/',add,name="add"),
    path('update/<str:category>/<int:id>/',update,name="update"),
    path('delete/<str:category>/<int:id>/',delete,name="delete")
]
