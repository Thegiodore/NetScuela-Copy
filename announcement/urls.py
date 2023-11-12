from django.urls import path
from .views import *

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='notifylist'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='notifydetail'),
    path('create/', AnnouncementCreateView.as_view(), name='notifycreate'),
]