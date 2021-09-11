from datetime import datetime
import random
from django.http import HttpResponse, FileResponse
from django.conf import settings
# Create your views here.
from django.shortcuts import render

from .models import Students, Blog


def hello_view(request):
    return render(request, 'register.html')


def date_view(request):
    today = datetime.now()
    return HttpResponse(f'Now: {str(today)}')


def random_number(request):
    num = random.randint(1, 1000)
    num1 = random.randint(1, num)
    num2 = random.randint(1, num1)
    num3 = random.randint(1, num2)
    num4 = random.randint(1, num3)
    context = {'num': num, 'numbers': [num1, num2, num3]}
    return render(request, 'random.html', context)


def image_view(request):
    path = settings.BASE_DIR / 'static' / 'brawl stars.jfif'
    file = open(path, 'rb')
    return FileResponse(file)


def student_view(request):
    students = Students.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def blog_view(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'blog.html', context)


def create_post(request):
        print(request.method)
        return render(request, 'create_post.html')