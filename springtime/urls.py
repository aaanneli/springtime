from django.conf.urls import url
from springtime import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^accounts/password/change/$', views.password_change, name='password_change'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^trampolines/$', views.trampolines, name='trampolines'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]