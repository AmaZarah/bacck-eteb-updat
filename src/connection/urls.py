from connection.views import index
from django.urls import path


app_name = "connection"

urlpatterns =[
    path('', index, name='connect') 
]
