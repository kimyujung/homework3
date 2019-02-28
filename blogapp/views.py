from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts })

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

@login_required
def blogpost(request):
    if request.method == 'POST' :
        form = BlogPost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.name = request.user.get_username()
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else :
        form = BlogPost()
        return render(request, 'new.html', {'form' : form})

@login_required        
def edit(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(pk = blog_id)
        form = BlogPost(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        blog = Blog.objects.get(pk=blog_id)
        form = BlogPost(instance=blog)
        return render(request, 'edit.html', {'blog':blog, 'form':form})
@login_required
def delete(request,blog_id):
    blog = Blog.objects.get(pk = blog_id)
    blog.delete()
    return redirect('home')