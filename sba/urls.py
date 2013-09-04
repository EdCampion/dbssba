from django.conf.urls import patterns, url

from sba import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)