from django.conf.urls import include, url
from neighborhoods import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
