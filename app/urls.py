from django.urls import path
from app.views import *

app_name = 'Virat'

urlpatterns=[
    path('RCB/',RCB,name='RCB')
]