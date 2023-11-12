from django import forms
from .models import Announcement

class AnnouncementModelForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['user','content']