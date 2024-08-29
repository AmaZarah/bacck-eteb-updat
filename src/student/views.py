from django.shortcuts import render, redirect
from .forms import FormStudent
from  .models import Student

# Create your views here.
def add_student(request):
    if request.method == "POST":
        form_student = FormStudent(request.POST)

        if form_student.is_valid():
            form_student.save()
            return redirect('student:liststudent')
        
    else:
      form_student = FormStudent()
    
    return render(request, 'add_student.html', {'form_student': form_student})

def edit_student(request, id):
    student = Student.objects.get(id = id)
    form_student = FormStudent(request.POST, instance=student)
    if form_student.is_valid():
       form_student.save()
       return redirect('student:liststudent')
    
    form_student = FormStudent(instance= student )
    return render(request, 'edit_student.html', {'form_user': form_student} )

    
def list_student(request):
    student = Student.objects.all()
    return render(request, 'list_student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id = id)
    student.delete()
    return redirect('student:liststudent')