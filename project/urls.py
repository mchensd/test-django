from django.conf.urls import url

from . import views

app_name=''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^increment/$', views.increment, name='increment'),
    url(r'^increment_delay/$', views.increment_delay_view, name='increment_delay'),


]