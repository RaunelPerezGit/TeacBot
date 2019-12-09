from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def main(request):
    return render(request, 'core/Main.html')

def courses(request):
    return render(request, 'core/Courses.html')

def course_detail(request):
    return render(request, 'core/Course_Detail.html')
