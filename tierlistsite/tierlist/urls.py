from django.urls import path
from . import views
from django.conf.urls import include, url
urlpatterns = [
    path('', views.index, name='index'),
    # url(regex=r'^api/fighters/$',
    #     view=views.list,
    #     name="fighters_api"
    #     ),
    url(r'api/',
        view=views.fighters_detail,
        name="fighters_api"
        )
    # path(r'^/fighters/$', views.fighters_list),
    # path(r'^/fighters/(?P<pk>[0-9]+)$', views.fighters_detail),
]