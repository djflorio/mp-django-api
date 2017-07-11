from django.conf.urls import url
from diner import views

urlpatterns = [
    url(r'^mbbpm/$', views.mb_bpm_list),
    url(r'^mbbpm/(?P<pk>[0-9]+)/$', views.mb_bpm_detail),
]