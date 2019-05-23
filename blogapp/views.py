from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator #빵칼
from .models import Blog

def home(request):
    blogs = Blog.objects.all().order_by('-id') #식빵
    #블로그의 모든 글을 대상으로 blog_,list에 넣어준다
    blog_list = Blog.objects.all().order_by('-id')
    #블로그 객체 세개를 한 페이지로 자르고
    paginator = Paginator(blog_list, 3) #어떤걸,몇개씩
    #request된 페이지가 뭔지를 알아내고 그걸 변수에 담는다
    page = request.GET.get('page')
    #request된 페이지를 얻은 뒤 출력해준다.
    posts = paginator.get_page(page) #식빵 조각들
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))