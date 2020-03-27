from django.conf.urls import url

from . import templates

urlpatterns = [
    url(r'^$', templates.hello),
]
