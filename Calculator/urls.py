from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/index/', views.index),
    url(r'^home/run/', views.run),
    url(r'^home/', views.home),
    url(r'^api/', views.api),
    url(r'^apitest', views.apitest)
]
