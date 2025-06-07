from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    record = Student.objects.all()
    context={
        'record':record
    }
    return render(request, 'index.html',context)

def student_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        date_of_birth = request.POST.get('date_of_birth')

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            marks=marks,
            date_of_birth=date_of_birth
        )

        return render(request, 'success.html',{'message':'Student added successfully'})
    
    return render(request, 'form.html')

def student_remove(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Filter the student(s)
        students = Student.objects.filter(first_name=first_name, last_name=last_name)

        if students.exists():
            students.delete()
            return render(request, 'success.html', {'message': 'Student(s) deleted successfully'})
        else:
            return render(request, 'success.html', {'message': 'No matching student found'})

    return render(request, 'del.html')


