from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Index page listing all post so far
    path('', views.index, name='index'),
    # Create a new post
    path('new_post/', views.new_post, name='new_post'),
    # Edit post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    # Show post
    path('post/<int:post_id>/', views.post, name='post')
]