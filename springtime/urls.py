from django.conf.urls import url
from springtime import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]