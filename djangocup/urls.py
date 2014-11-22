from django.conf.urls import patterns, include, url
from django.contrib import admin

from cups import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangocup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^', include('cups.urls')),
    # url(r'^$', views.index, name="index"),
)
