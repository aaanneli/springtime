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
    url(r'^accounts/password/change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^accounts/register/complete/$', views.user_registered, name='registration_complete'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^trampolines/$', views.trampolines, name='trampolines'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]