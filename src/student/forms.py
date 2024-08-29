

from django import forms

from student.models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=50)
#     classe = forms.CharField(max_length=50)
#     birth_day = forms.DateField(max_length=10)
#     sex = forms.CharField(max_length=15)
#     town = forms.CharField(max_length=20)
#     phone = forms.CharField(max_length=30)
#     registration_number= forms.CharField(max_length=20)


#formulaire lié
class FormStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"