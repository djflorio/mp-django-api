from django.conf.urls import url
from diner import views

urlpatterns = [
    url(r'^mbbpm/$', views.mb_bpm_list),
    url(r'^mbbpm/(?P<pk>[0-9]+)/$', views.mb_bpm_detail),
    url(r'^metadata/$', views.metadata_list),
    url(r'^metadata/(?P<pk>[0-9]+)/$', views.metadata_detail),
]