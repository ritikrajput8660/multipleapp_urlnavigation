from django.urls import path
from app2.views import *

app_name= 'Msd'

urlpatterns = [
    path('csk/',csk,name='csk')
]