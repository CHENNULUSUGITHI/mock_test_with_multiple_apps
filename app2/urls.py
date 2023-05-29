from django.urls import path
from app2.views import *
app1_name='anything'
urlpatterns=[
    path('mock2/',mock2,name='mock2'),
]
