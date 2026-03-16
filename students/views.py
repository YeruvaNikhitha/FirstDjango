from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Read
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

# Create
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        Student.objects.create(name=name, email=email, course=course)
        return redirect('student_list')
    return render(request, 'students/add.html')

# Update
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'students/edit.html', {'student': student})

# Delete
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')