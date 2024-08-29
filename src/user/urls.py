from django.urls import path
from user.views import add_user, edit_user, list_user, delete
  


app_name = "user"

urlpatterns =[
    path('',add_user, name='adsuser'),
    path('listuser',list_user, name='listuser' ),
    path('edituser/<int:id>/', edit_user, name='edituser'),
    path('delete/<int:id>/', delete, name='del')
   
]