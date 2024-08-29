
from dashboard.views import index
from dashboard.views import login
from django.urls import path


app_name = "dashboard"

urlpatterns =[
    path('/dashboard', index, name='index'),
    path('', login, name='login')
]   