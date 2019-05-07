from django.conf.urls import url
from django.contrib import admin
from etv import views as v1
from tornado import views as v2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', v1.index, name='home'),
    url(r'^quakes/', v1.quakes, name='quakes'),
    url(r'^tsunami/', v1.tsunami, name='tsunami'),
    url(r'^volcano/', v1.volcano, name='volcano'),
    url(r'^tornado/', v2.tornado, name='tornado'),
]

admin.site.site_url = '/home'
