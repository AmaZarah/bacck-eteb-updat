
from django import forms

from teacher.models import Teacher




#formulaire non lié

# class TeacherForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
#     subject = forms.CharField(max_length=50 )
#     birth_day = forms.DateField()
#     sex = forms.CharField(max_length=15)
#     town = forms.CharField(max_length=20)
#     phone = forms.CharField(max_length=30)




#formulaire lié
class FormTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'