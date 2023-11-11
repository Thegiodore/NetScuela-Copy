from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Announcement
from .forms import AnnouncementModelForm

class AnnouncementListView(ListView):
    queryset = Announcement.objects.all()
    template_name = 'announcementlist.html'

class AnnouncementDetailView(DetailView):
    template_name = 'announcementdetail.html'

    def get_object(self, query=Announcement.objects.all()):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        return Announcement.objects.get(id=pk)


class AnnouncementCreateView(CreateView):
    template_name = 'announcementcreate.html'
    form_class = AnnouncementModelForm
    success_url = "/"

# Create your views here.
