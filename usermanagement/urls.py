from django.conf.urls import url

from . import views

app_name = 'usermanagement'

urlpatterns = [
        url(r'^$', views.UserList.as_view(), name = 'user_list'),
        url(r'^new$', views.UserCreate.as_view(), name="user_new"),
        url(r'^edit/(?P<pk>[a-zA-Z0-9_.-]+)/$', views.UserUpdate.as_view(), name="user_edit"),
        url(r'^(?P<pk>[a-zA-Z0-9_.-]+)/$', views.DetailView.as_view(), name="detail"),
]