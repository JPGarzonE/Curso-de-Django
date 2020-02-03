"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world, name = 'hello_world'),
    path('sort/', local_views.sorted_numbers, name = 'sort'),
    path('welcome/<str:name>/<int:age>', local_views.greet_user, name = 'greeting'),

    path('posts/', posts_views.list_posts, name = 'feed'),

    path('users/login/', users_views.login_view, name = 'login'),
    path('users/logout/', users_views.logout_view, name = 'logout'),

] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
