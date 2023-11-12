from django.urls import path
from NetScuela.views import create_posts
from . import views
from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create_posts/', create_posts, name='create_blog'),
    path('add_post/', views.add_post, name='add_post'),
]
