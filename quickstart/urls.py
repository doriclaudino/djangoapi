from django.conf.urls import url
from quickstart import views

urlpatterns = [
    url(r'^person/$', views.person_list, name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.person_detail, name='person_detail'),
]
