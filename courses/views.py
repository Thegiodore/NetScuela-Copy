from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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

class CourseUpdateView(StaffRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_create.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})

class CourseDeleteView(StaffRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')

class AssignmentCreateView(StaffRequiredMixin, CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment_create.html'

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.kwargs['course_id']})

    def form_valid(self, form):
        form.instance.course = Course.objects.get(pk=self.kwargs['course_id'])
        return super().form_valid(form)

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_detail.html'
    context_object_name = 'assignment'

    def post(self, request, *args, **kwargs):
        assignment = self.get_object()
        file_upload = request.FILES.get('file_upload')

        if file_upload:
            assignment.file_upload = file_upload
            assignment.save()

        return super().get(request, *args, **kwargs)

class AssignmentDeleteView(StaffRequiredMixin, DeleteView):
    model = Assignment
    template_name = 'assignment_delete.html'
    success_url = reverse_lazy('course_list')

def todo_list(request):
    current_assignments = Assignment.objects.filter(deadline__gte=timezone.now())
    return render(request, 'todo_list.html', {'current_assignments': current_assignments})