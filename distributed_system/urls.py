from django.contrib import admin
from django.urls import path
from .views import checkBalance,transfer

urlpatterns = [
    path('checkBalance/<int:id>/',checkBalance,name='checkBalance'),
    path('transfer/',transfer,name='transfer'),
    # path('test/',test,name='test'),
]