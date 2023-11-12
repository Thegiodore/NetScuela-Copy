from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Assignment
from .forms import CourseForm, AssignmentForm
from django.urls import reverse_lazy

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_create.html'
    success_url = '/courses/'

class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_create.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.kwargs['course_id']})

    def form_valid(self, form):
        form.instance.course = Course.objects.get(pk=self.kwargs['course_id'])
        return super().form_valid(form)