from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AccountCreationForm, DepositForm, WithdrawForm, TransferForm
from .models import Accounts,Transfer
from django.contrib import messages


# Create your views here.
def create_account(request):
    form = AccountCreationForm()
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('customerlogin')
        else:
            context["form"] = form
            return render(request, "createaccount.html", context)

    return render(request, "createaccount.html", context)


# def customer_login(request):
#     context = {}
#     if request.method=='POST':
#         email=request.POST.get('email')
#         pin=request.POST.get('pin')
#         # customer=authenticate(request, email=email,Account_pin=pin)
#         customer=Accounts.objects.get(email=email)
#         print(pin,customer.Account_pin)
#         if pin != customer.Account_pin:
#             context.update({'alert': "wrong pin"})
#         queryset = Accounts.objects.filter(email=email)
#         print(queryset)
#         context["details"] = queryset
#         return render(request,"customerhome.html",context)
#     return render(request, "login.html")

def customer_login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        pin = request.POST.get('pin')
        try:
            # customer=Accounts.objects.get(email=email,Account_pin=pin)
            queryset = Accounts.objects.filter(email=email, Account_pin=pin)
            print(queryset)
            context["details"] = queryset
            return render(request, "customerhome.html", context)
        except:
            messages.info(request, 'invalid credentials')
            return render(request, "login.html", context)

    return render(request, "login.html")


def deposit_amount(request,pk):
    context = {}
    form = DepositForm()
    context["form"] = form
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('deposit_amount')
            account_pin=request.POST.get('Account_pin')
            customer = Accounts.objects.get(id=pk)
            balance = customer.balance_amount
            new_balance = balance + int(amount)
            context["amount"] = amount
            context["balance"] = new_balance
            Accounts.objects.filter(id=pk).update(balance_amount=new_balance)
            return render(request, "depositsuccess.html", context)
        else:
            context["form"] = form
            return render(request, 'depositamount.html', context)

    return render(request, 'depositamount.html', context)


def withdraw_amount(request, pk):
    context = {}
    form = WithdrawForm()
    context["form"] = form
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('withdraw_amount')
            customer = Accounts.objects.get(id=pk)
            balance = customer.balance_amount
            if int(amount) >= balance or balance <= 500:
                print(int(amount) >= balance or balance <= 500)
                messages.info(request, 'insufficient Balance')
                return render(request, 'withdrawamount.html', context)

            new_balance = balance - int(amount)
            context["amount"] = amount
            context["balance"] = new_balance
            Accounts.objects.filter(id=pk).update(balance_amount=new_balance)
            return render(request, "withdrawsuccess.html", context)
        else:
            context["form"] = form
            return render(request, 'withdrawamount.html', context)

    return render(request, 'withdrawamount.html', context)


def transfer_amount(request, pk):
    context = {}
    account_no = Accounts.objects.get(id=pk).Account_no
    form = TransferForm(initial={'Account_no': account_no})
    context["form"] = form
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            from_balance = Accounts.objects.get(id=pk).balance_amount
            amount = request.POST.get('amount')
            to_account = request.POST.get('to_account')
            to_balance = Accounts.objects.get(Account_no=to_account).balance_amount
            print(from_balance)
            print(to_balance)
            from_balance -= int(amount)
            to_balance += int(amount)
            Accounts.objects.filter(id=pk).update(balance_amount=from_balance)
            Accounts.objects.filter(Account_no=to_account).update(balance_amount=to_balance)
            form.save()
            context["balance"] = from_balance
            context["amount"] = amount
            context["account"] = to_account

            return render(request, "transfersuccess.html", context)
        else:
            context["form"] = form
            return render(request, "transferamount.html", context)

    return render(request, "transferamount.html", context)


def view_balance(request, pk):
    context = {}
    balance = Accounts.objects.get(id=pk).balance_amount
    context["balance"] = balance
    return render(request, "viewbalance.html", context)


def transfer_history(request,pk):
    context={}
    account_no=Accounts.objects.get(id=pk).Account_no
    print(account_no)
    query_set=Transfer.objects.filter(Account_no=account_no)
    context["details"]=query_set
    print(query_set)
    return render(request, "transferhistory.html", context)

