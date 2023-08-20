from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
# Register your models here.

class CustumUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_superuser', 'is_active')
    list_filter = ('email', 'username', 'is_superuser', 'is_active')
    search_fields = ('email' , 'username','is_active')
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                "email", 'username', "password"),}),
        ('Permissions', {
            "fields": (
                "is_staff", "is_superuser","is_active"),}),
        ('Group Permissions', {
            "fields": (
                "groups", "user_permissions"),}),
        ('Important date', {
            "fields": (
                "last_login",),})
    )
    
    
    add_fieldsets = (
        (None, {
            "fields": (
                "email", 'username', "password1", "password2", "is_staff",
                "is_active","groups", "user_permissions"
            )}
        ),
    )
    
    




admin.site.register(CustomUser,CustumUserAdmin)
