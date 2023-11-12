from django.urls import path
from .views import CourseListView, CourseDetailView, CourseCreateView, AssignmentCreateView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:course_id>/create_assignment/', AssignmentCreateView.as_view(), name='assignment_create')
]