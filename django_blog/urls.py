from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='home'),

    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.date_archive', name="blog_date_archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.category_archive', name="blog_category_archive"),
    url('^blog/(?P<slug>[-\w]+)/$', 'blog.views.single', name="blog_article_single"),
    url('^blog/$', 'blog.views.index', name="blog_article_index"),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
