from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.


def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
    form = PostForm()
    context = {
        'form': form,
    }
    template = 'post/post_create.html'
    return render(request, template, context)


def post_list_view(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post,
    }
    template = 'post/post_list.html'
    return render(request, template, context)


def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    template = 'post/post_detail.html'
    return render(request, template, context)


def post_update_view(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail', id=post.id)
    context = {
        'form': form,
    }
    template = 'post/post_update.html'
    return render(request, template, context)
