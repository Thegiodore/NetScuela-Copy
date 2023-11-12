from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/new/', course_new, name='course_new'),
    path('course/<int:pk>/edit/', course_edit, name='course_edit'),
    path('course/<int:pk>/delete/', course_delete, name='course_delete'),
]