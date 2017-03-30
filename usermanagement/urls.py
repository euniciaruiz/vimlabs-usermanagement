from django.conf.urls import url

from . import views

app_name = 'usermanagement'

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name = 'index'),
        url(r'^(?P<pk>[a-zA-Z0-9_.-]+)/$', views.DetailView.as_view(), name="detail"),
]