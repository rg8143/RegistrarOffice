from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/$', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^directorOffice/$', views.directorOffice, name='directorOffice'),
    url(r'^officeOfRegistrar/upload/$', views.upload, name='uploaddoc'),
    url(r'^officeOfRegistrar/generalAdminForm/reject/$', csrf_exempt(views.admin_reject), name='admin_reject'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^officeOfDeanPnD/', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),

]
