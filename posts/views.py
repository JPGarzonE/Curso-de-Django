"""Posts views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Model
from posts.models import Post

# Forms
from posts.forms import PostForm

# Class-based views
class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = 'posts/feed.html'
    model = Post
    context_object_name = 'posts'
    ordering = ('-created',)
    paginate_by = 20

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return and render the detail of a post"""

    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        kwargs = self.get_form_kwargs()

        post = self.request.POST.copy()
        post['user'] = self.request.user
        post['profile'] = self.request.user.profile

        kwargs.update({'data': post})

        if form_class is None:
            form_class = self.get_form_class()
            
        return form_class(**kwargs)

# Function views

# @login_required
# def create_post(request):
#     """Create a new post"""

#     if request.method == 'POST':
        
#         form_data = {
#         'user': request.user.pk,
#         'profile': request.user.profile.pk,
#         'title': request.POST.get('title', False)
#         }
        
#         form = PostForm( form_data, request.FILES )
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
        
#     else:
#         form = PostForm()

#     return render(
#         request = request,
#         template_name = 'posts/new.html',
#         context = {
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )