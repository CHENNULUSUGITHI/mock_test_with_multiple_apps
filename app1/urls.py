from django.urls import path
from app1.views import *
app1_name='anything'
urlpatterns=[
    path('mock1/',mock1,name='mock1'),
]

