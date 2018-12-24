from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^/fighters/$', views.fighters_list),
    url(r'^api/fighters/(?P<pk>[0-9]+)$', views.fighters_detail),
]