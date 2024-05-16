from django.shortcuts import render
from apps.base.models import *


def infor(requests):
       user = User.objects.all()
       return render(requests, 'demo-academic.html', locals())

# Create your views here.
