from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^(?P<hash_code>)/$', views.user_detail, name='detail'),
]