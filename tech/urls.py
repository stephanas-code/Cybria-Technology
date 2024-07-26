from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('', index, name='index'),
    path('becomeadeveloper', becomeadeveloper, name='becomeadeveloper' )

]