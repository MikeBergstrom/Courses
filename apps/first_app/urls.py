from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newcourse$', views.newcourse),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^addcomment/(?P<id>\d+)$', views.addcomment)
]