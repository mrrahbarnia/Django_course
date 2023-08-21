"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.contrib.auth import views as auth_view
from website import views as website_views
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path("blog/",include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    # =============== Urls for reseting password if user forgot the password =============== #
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html'), name='reset_password'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name='password_reset_complete'),
    # =============== Urls for changing password while user is authenticated =============== #
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name = 'accounts/password_change_form.html'), name='password_change'),
    path('password_change_done', auth_view.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'), name='password_change_done'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.MAINTENANCE_MODE:
    urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='coming-soon.html'), name='coming-soon'))