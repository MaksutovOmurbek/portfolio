from django.urls import path
from apps.base.views import infor

urlpatterns = [
    path('', infor, name ='demo_academic_url')
]