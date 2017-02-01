from django.conf.urls import include, url
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    
    url(r'^$', views.post_list),
    url (r'^post/(?P<pk>[0-9]+)/$', views.post_detail)
]
