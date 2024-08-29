
from django import forms
from .models import  User


# formulaire non lies

# class UserForm(forms.Form):
#     pseudo =forms.CharField(max_length=10, unique=True)
#     pass_word = forms.CharField(max_length=128)
#     creat_dat = forms.DateField(auto_now_add=True)


#formulaire lies
class FormUser(forms.ModelForm):
    class Meta:
       model = User
       fields = "__all__"
       widgets = {
           'pass_word': forms.PasswordInput(),
       }