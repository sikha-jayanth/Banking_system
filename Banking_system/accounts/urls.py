from django.shortcuts import render
from django.urls import path

from accounts.views import create_account, customer_login, deposit_amount, withdraw_amount, transfer_amount, \
    view_balance, transfer_history

urlpatterns = [

    path('create', create_account, name="create"),
    path('login', customer_login, name='customerlogin'),
    path("home", lambda request: render(request, "customerhome.html"), name="customerhome"),
    path('deposit<int:pk>', deposit_amount, name='deposit'),
    path('withdraw<int:pk>', withdraw_amount, name='withdraw'),
    path('transfer<int:pk>', transfer_amount, name='transfer'),
    path('view_balance<int:pk>', view_balance, name='view_balance'),
    path('transfer_history<int:pk>',transfer_history,name='transfer_details'),

]
