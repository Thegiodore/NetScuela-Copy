from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    ACCOUNT_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, label='Account Type')
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if self.cleaned_data['account_type'] == 'teacher':
            user.is_staff = True
        else:
            user.is_staff = False

        if commit:
            user.save()
        return user