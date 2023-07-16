from django.contrib import admin
from website.models import Contact,Newslettter

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

@admin.register(Newslettter)
class NewsletterAdmin(admin.ModelAdmin):
    pass