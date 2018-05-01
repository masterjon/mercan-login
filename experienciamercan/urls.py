from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'experienciamercan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', auth_views.login,{'template_name': 'base.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
