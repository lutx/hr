from django.conf.urls import url
from django.urls import reverse
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^emp/$', views.employee, name='emp'),
    url(r'^emp/(?P<id>\d+)/$', views.employee_details, name='employee_details'),
]
