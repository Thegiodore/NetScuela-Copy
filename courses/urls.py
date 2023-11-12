from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:pk>/', course_detail, name='course_detail'),
    path('create/', course_create, name='course_create'),
    path('<int:pk>/edit/', course_edit, name='course_edit'),
    path('<int:pk>/delete/', course_delete, name='course_delete'),
]