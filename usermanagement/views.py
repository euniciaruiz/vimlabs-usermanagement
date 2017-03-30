from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import User
# Create your views here.

      
class IndexView(generic.ListView):
        template_name = 'usermanagement/index.html'
        context_object_name = 'user_list'

        def get_queryset(self):
                return User.objects.all()

class DetailView(generic.DetailView):
        model = User
        template_name = 'usermanagement/detail.html'
