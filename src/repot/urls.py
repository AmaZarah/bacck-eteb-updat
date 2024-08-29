from repot.views import index
from django.urls import path


app_name = "repot"

urlpatterns =[
    path('', index, name='rappt') 
]