from django.shortcuts import render
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
    return render (request, 'calendar.html')

def account_settings(request):
    return render (request, 'account_settings.html')

def mail(request):
    return render (request, 'mail.html')

def announcement(request):
    return render (request, 'announcementlist.html')
