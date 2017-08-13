from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^controller/', include('motorcontroller.urls')),
    url('^', include('django.contrib.auth.urls')),
    # url(r'^login/$', auth_views.login, kwargs={'redirect_authenticated_user': True}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/controller/login/'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset),
    url(r'^password_reset/done/$', auth_views.password_reset_done),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm),
    url(r'^reset/done/$', auth_views.password_reset_complete),
]
