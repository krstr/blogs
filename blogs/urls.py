"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a post.
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post')
    
]

