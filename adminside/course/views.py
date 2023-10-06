from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm 
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def course_view(request):
    courses=Course.objects.all()
    return render(request,'course.html',{'courses':courses})


def addCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('courses')  
    else:
        form = CourseForm()

    return render(request, 'addCourse.html', {'form': form})


def active_courses(request):
    active_courses = Course.objects.filter(active=True).values('title', 'subtitle', 'image')    
    return JsonResponse({'active_courses': list(active_courses)})

def inactive_courses(request):
    inactive_courses = Course.objects.filter(active=False).values('title','subtitle','image')
    return JsonResponse({'inactive_courses': list(inactive_courses)})

def EditCourse(request, id):
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)

        if form.is_valid():
            form.save()
            messages.success(request, 'Course edited successfully.')
            return redirect('courses')
        else:
            messages.error(request, 'Invalid input')
    
    
    form = CourseForm(instance=course)
    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'EditCourse.html', context)


def deleteCourse(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  messages.success(request, 'Course deleted successfully.')
  return redirect('courses')




