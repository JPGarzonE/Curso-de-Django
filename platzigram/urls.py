"""Platzigram URLs module."""

#Django
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world),
    path('sort/', local_views.sorted_numbers),
    path('welcome/<str:name>/<int:age>', local_views.greet_user),

    path('posts/', posts_views.list_posts),
]
