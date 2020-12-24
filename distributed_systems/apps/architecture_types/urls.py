from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<architecture_type_id>[0-9]+)/$', views.detail, name='detail'),
]
