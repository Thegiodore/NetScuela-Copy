from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import EmailForm

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('emailform.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            send_mail('The email form subject', 'Missio est', 'noreply@hotmail.com', ['mgl3185473@gmail.com'], html_message=html)
            #third parameter is the sender, fourth is the recipient

            return redirect('email')
    else:
        form = EmailForm()
    return render(request, 'email.html', {
        'form': form
    })
# Create your views here.
