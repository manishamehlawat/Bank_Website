from django.conf.urls import url
from . import views

app_name='user_dashboard'
urlpatterns=[
    url('deposit/',views.deposite,name='deposit'),
    url('withdraw/',views.withdrawal,name='withdraw'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('logout/',views.logout,name='logout'),
    
    
    ]