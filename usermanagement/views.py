from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from django.core.urlresolvers import reverse_lazy
# Create your views here.

      
class UserList(generic.ListView):
        model = User

class DetailView(generic.DetailView):
        model = User
        template_name = 'usermanagement/detail.html'

class UserCreate(CreateView):
        model = User
        fields = ['user_name', 'role', 'email']
        success_url = reverse_lazy('usermanagement:user_list')

class UserUpdate(UpdateView):
        model = User
        fields = ['user_name', 'role', 'email']
        success_url = reverse_lazy('usermanagement:user_list')