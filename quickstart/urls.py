from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views


urlpatterns = [
    url(r'^person/$', views.PersonList.as_view(), name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$',
        views.PersonDetail.as_view(), name='person_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
