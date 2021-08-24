from screener.forms import BlogForm
from django.shortcuts import get_object_or_404, redirect, render
from screener import models

# Create your views here.
def index(request):
    return render(request,'index.html')

def news(request):
    return render(request,'news.html')

def blogs(request):
    blogs = models.Blog.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})

def dashboard(request):
    blogs = models.Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'dashboard.html',context)

def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BlogForm()
    return render(request,'new_blog.html',{'form':form})

def edit_blog(request,blog_id=None):
    item = get_object_or_404(models.Blog,id=blog_id)
    form = BlogForm(instance=item)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('test')
    return render(request,'edit_blog.html',{'form':form})

def view_blog(request,slug):
    blogs = models.Blog.objects.all()
    return render(request,'blogpost.html',{'article':get_object_or_404(models.Blog,slug=slug),'blogs':blogs})

def delete_blog(request,blog_id=None):
    blog = get_object_or_404(models.Blog,id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('dashboard')
    return render(request,'delete_blog.html',{'blog':blog})