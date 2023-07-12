from django import template
from blog.models import Post,Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latestposts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-postcategories.html')
def post_categories():
    posts = Post.objects.filter(published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}