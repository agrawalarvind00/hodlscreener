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
    num = len(blogs)
    print(num)
    for i in range(0,num,2):
        print(i)
        print(i+1)
    return render(request,'blogs.html',{'blogs':blogs, 'num':num})

def test(request):
    obj = models.Blog.objects.all()
    context = {'obj':obj}
    return render(request,'image.html',context)

def test2(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('test')
    else:
        form = BlogForm()
    return render(request,'test2.html',{'form':form})

def test3(request,blog_id=None):
    item = get_object_or_404(models.Blog,id=blog_id)
    form = BlogForm(instance=item)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('test')
    return render(request,'test2.html',{'form':form})