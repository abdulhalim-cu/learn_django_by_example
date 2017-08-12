from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^controller/', include('motorcontroller.urls')),
    url('^', include('django.contrib.auth.urls')),
]
