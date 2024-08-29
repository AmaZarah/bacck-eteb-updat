from django.shortcuts import render, redirect
#from .forms import TeacherForm
from .forms import FormTeacher
from .models import Teacher

# Create your views here.
def add_teacher(request):
    if request.method == "POST":
        form_teache = FormTeacher(request.POST)
        if form_teache.is_valid():
            form_teache.save()
        
    else:
      form_teache = FormTeacher()
    
    return render(request, 'add_teacher.html', {'form_teache': form_teache} )

def edit_teacher(request, id):
    teacher = Teacher.objects.get(id = id)
    form_teache = FormTeacher(request.POST, instance=teacher)
    if form_teache.is_valid():
       form_teache.save()
       return redirect('teacher:llistteacher')
    
    form_teache = FormTeacher(instance= teacher )
    return render(request, 'edit_teacher.html', {'form_teache': form_teache} )

    

def list_teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'list_teacher.html', {'teacher': teacher})


def delete_teacher(request, id):
    teacher = Teacher.objects.get(id = id)
    teacher.delete()
    return redirect('teacher:llistteacher')
