from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image
    # tag
    # category
    # author
    counted_views = models.ImageField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null = True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

