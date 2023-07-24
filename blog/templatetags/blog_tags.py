from django import template
from blog.models import Post,Category,Comment
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latestposts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-postcategories.html')
def popular_categories():
    posts = Post.objects.filter(published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    cat_dict = dict((sorted(list(cat_dict.items()),key=lambda x:x[1],reverse=True)[:5]))
    
    return {'categories':cat_dict}

@register.simple_tag(name="comments_counter")
def function(pid):
    post = Post.objects.get(pk=pid,status=True)
    return Comment.objects.filter(post=post,approved = True).count()



