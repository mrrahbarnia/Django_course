from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts,3)
    page_number = request.GET.get('page')
    try:
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,published_date__lte = timezone.now())
    context = {'post':post}
    post.counted_views += 1
    post.save()
    return render(request,'blog/blog-single.html',context)

def search_bar(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

