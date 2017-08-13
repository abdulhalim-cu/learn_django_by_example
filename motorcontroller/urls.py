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
    url(r'^register_device/$', views.register_device, name='register_device'),
    url(r'^password_change/$', auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^password_reset/$', auth_views.password_reset),
    # url(r'^password_reset/done/$', auth_views.password_reset_done),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm),
    # url(r'^reset/done/$', auth_views.password_reset_complete),
]