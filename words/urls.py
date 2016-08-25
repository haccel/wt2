from django.conf.urls import url

from . import views

app_name = 'words'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^created$', views.created, name='created'),
]