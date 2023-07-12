from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category
from django.utils import timezone

# Create your views here.
def blog_view(request,cat_name=None):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,published_date__lte = timezone.now())
    context = {'post':post}
    post.counted_views += 1
    post.save()
    return render(request,'blog/blog-single.html',context)