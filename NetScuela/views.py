from django.shortcuts import render

from Blog.models import Post


def home(request):
    return render(request, 'home.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    return render(request, 'account/login.html')


def register(request):
    return render(request, 'account/register.html')


def calendar(request):
    return render(request, 'calendar.html')


def account_settings(request):
    return render(request, 'account_settings.html')


def mail(request):
    return render(request, 'mail.html')


def announcement(request):
    return render(request, 'announcementlist.html')


def todo_checklist(request):
    return render(request, 'todo_checklist.html')



def courses(request):
    return render(request, 'course_list.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def blog(request):
    return render(request, 'Blog.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Blog/post_list.html', {'posts': posts})


def create_posts(request):
    return render(request, 'Blog/create_blog.html')
