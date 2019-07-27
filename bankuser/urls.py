from django.conf.urls import url
from . import views

app_name='bankuser'
urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
   
    ]