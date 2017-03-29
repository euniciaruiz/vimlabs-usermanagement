from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.

def index(request):
        user_list = User.objects.all()
        context = {
                'user_list': user_list 
        }
        return render(request, 'usermanagement/index.html', context)

def user_detail(request, user_id):
        return HttpResponse("You're looking at user: %s" % user_id)

