from os import name
from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'ugamix'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.AllMovies, name='AllMovies'),

]