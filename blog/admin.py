from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_vallue_display = '-empty-'
    list_display = ('title','counted_views','status','published_date','created_date')
    list_filter = ('status',)
    search_fields = ('title','content')
    



