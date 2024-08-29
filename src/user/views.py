from django.shortcuts import render, redirect
from .forms import FormUser
from .models import User

# Create your views here.
def add_user(request):
    if request.method == 'POST':
        form_user = FormUser(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('user:listuser')
        
    else:
      form_user = FormUser() 
        

    return render(request, 'add_user.html', {'form_user': form_user} )

def edit_user(request, id): 
    user = User.objects.get(id = id)
    form_user = FormUser(request.POST, instance= user)
    if form_user.is_valid():
       form_user.save()
       return redirect('user:listuser')

    form_user = FormUser(instance= user )
    return render(request, 'edit_user.html', {'form_user': form_user} )

def list_user(request):
    user = User.objects.all()
    return render(request, 'list_user.html', {'user': user})


def delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('user:listuser')
 