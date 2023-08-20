from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



def blog_view(request,**kwargs):
    posts = Post.objects.filter(status = True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your comment submitted successfully")
        else:
            messages.error(request,"Your comment didn't submit")
    post = get_object_or_404(Post,pk=pid,status = True)
    comments = Comment.objects.filter(post=post,approved = True)
    form = CommentForm()
    context = {'post':post,'comments':comments,'form':form}
    post.counted_views += 1
    post.save()
    if not post.login_require:
        return render(request,'blog/blog-single.html',context)
    else:
        if request.user.is_authenticated:
            return render(request,'blog/blog-single.html',context)
        else:
            messages.info(request,"You must login first to see special posts.")
            return HttpResponseRedirect(reverse('accounts:login'))
            
    

def search_bar(request):
    posts = Post.objects.filter(pstatus = True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

