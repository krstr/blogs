from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost 
from .forms import PostForm

def check_post_owner(request, post):
    if post.owner != request.user:
        raise Http404
    else:
        pass

# Create your views here.
def index(request):
    """The home page for blog and shows all posts."""
    posts = BlogPost.objects.order_by('date_added')
    # texts = []
    # for post in posts:
    #     text = post.text
    #     texts.append(text)
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            form.save()
            return redirect('blogs:index')
            
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing entry."""
    post = BlogPost.objects.get(id=post_id)
    check_post_owner(request, post)
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
            
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


   