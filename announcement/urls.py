from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='notifylist'),
    re_path(r'^(?P<pk>\d)/$', AnnouncementDetailView.as_view(), name='notifydetail'),
    path('create/', AnnouncementCreateView.as_view(), name='notifycreate'),
]