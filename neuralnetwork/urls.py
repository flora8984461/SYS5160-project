# -*- coding: utf-8 -*-
#neuralnetwork/urls.py

from django.urls import path
from . import views

app_name = 'neuralnetwork'
app_name='newnural'

urlpatterns = [
    path('',views.index,name='index'),
]