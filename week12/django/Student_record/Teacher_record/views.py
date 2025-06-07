from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teacherindex(request):
    record = Teacher.objects.all()
    context={
        'record':record
    }
    return render(request, 'teacher__record/teacherindex.html', context)

def teacher_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        join_date = request.POST.get('join_date')
        salary = request.POST.get('salary')

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            join_date=join_date,
            salary=salary
        )

        return render(request, 'teacher__record/teachersuccess.html',{'message':'Teacher added successfully'})
    
    return render(request, 'teacher__record/teacherform.html')

def teacher_remove(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Filter the student(s)
        teacher = Teacher.objects.filter(first_name=first_name, last_name=last_name)

        if teacher.exists():
            teacher.delete()
            return render(request, 'teacher__record/teachersuccess.html', {'message': 'Teacher(s) deleted successfully'})
        else:
            return render(request, 'teacher__record/teachersuccess.html', {'message': 'No matching teacher found'})

    return render(request, 'teacher__record/teacherdel.html')


