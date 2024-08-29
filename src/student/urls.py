from django.urls import path
from student.views import add_student, edit_student, list_student, delete_student
  


app_name = "student"

urlpatterns =[
    path('',add_student, name='adstudent'),
    path('liststudent',list_student, name='liststudent' ),
    path('editstudent/<int:id>/',edit_student, name='editstudent'),
    path('delete/<int:id>/', delete_student, name='delstud')
   
]