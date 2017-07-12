from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from diner import views

urlpatterns = [
    url(r'^mbbpm/$', views.MbBpmList.as_view()),
    url(r'^mbbpm/(?P<pk>[0-9]+)/$', views.MbBpmDetail.as_view()),
    url(r'^metadata/$', views.MetadataList.as_view()),
    url(r'^metadata/(?P<pk>[0-9]+)/$', views.MetadataDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)