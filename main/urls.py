from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^getAPIRequests/$', views.ajaxGetAPIRequests, name='get_api_requests'),
]