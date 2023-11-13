from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import Announcement
from .forms import AnnouncementModelForm
from django.urls import reverse_lazy
from NetScuela.mixins import StaffRequiredMixin

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcementlist.html'
    context_object_name = 'announcements'

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcementdetail.html'
    context_object_name = 'announcement'

class AnnouncementCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Announcement
    template_name = 'announcementcreate.html'
    form_class = AnnouncementModelForm
    success_url = "/announcement/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnnouncementDeleteView(StaffRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'announcementdelete.html'
    success_url = reverse_lazy('notifylist')

# Create your views here.
