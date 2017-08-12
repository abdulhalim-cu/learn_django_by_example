from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'motorcontroller'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, kwargs={'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/controller/login/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url('^', include('django.contrib.auth.urls')),
]