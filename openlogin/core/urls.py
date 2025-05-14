
from django.urls import path
from . import auth
urlpatterns=[
    path('login/', auth.login, name='login'),
    path('logout/', auth.logout, name='logout'),
]