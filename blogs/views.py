"""View functions for blogs app."""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm


def index(request):
    """Index page with all blogs."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def post(request, post_id):
    """Show a particular post."""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)


@login_required
def new_post(request):
    """Create post."""
    if request.method != 'POST':
        """No data passed; create an empty form."""
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')

    # Display a blank form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        """Just opened an editing page."""
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)
