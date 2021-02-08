from django import forms
from django.forms import ModelForm
from.models import Accounts,Transfer
from django import forms
class AccountCreationForm(ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"
        widgets = {
            "Account_no": forms.TextInput(attrs={'class': "form-control"}),
            "Customer_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "Account_pin": forms.PasswordInput(attrs={'class': "form-control"}),
            "balance_amount":forms.NumberInput(attrs={'class': "form-control"}),
            "date_opened":forms.HiddenInput()
        }
    def clean(self):
        cleaned_data=super().clean()
        balance= cleaned_data.get('balance_amount')
        if balance<500:
            msg = "Enter an amount greater than 500"
            self.add_error('balance_amount', msg)

class DepositForm(forms.Form):
    deposit_amount = forms.IntegerField()

    def clean(self):
        cleaned_data=super().clean()
        amount= cleaned_data.get('deposit_amount')
        if amount<100:
            msg = "Minimum deposit amount 100"
            self.add_error('deposit_amount', msg)


class WithdrawForm(forms.Form):
    withdraw_amount=forms.IntegerField()

    def clean(self):
        cleaned_data=super().clean()
        amount= cleaned_data.get('withdraw_amount')
        account_pin=cleaned_data.get('withdraw_amount')
        if amount<100:
            msg = "Minimum withdraw amount"
            self.add_error('withdraw_amount', msg)


class TransferForm(ModelForm):
    class Meta:
        model=Transfer
        fields="__all__"
        widgets={
            "Account_no": forms.HiddenInput(),
            "to_account":forms.TextInput(attrs={'class': "form-control"}),
            "amount":forms.NumberInput(attrs={'class': "form-control"}),
            "date_of_transfer":forms.HiddenInput()

        }
    def clean(self):
        cleaned_data=super().clean()
        amount= cleaned_data.get('amount')
        account_no=cleaned_data.get('to_account')
        balance=0


        try:
            customer=Accounts.objects.get(Account_no=account_no)
            balance = Accounts.objects.get(Account_no=account_no).balance_amount

        except:
            msg = "Account Doesn't exists"
            self.add_error('to_account', msg)




        if amount<100:
            msg = "Enter an amount greater than 100"
            self.add_error('amount', msg)
        if amount>balance:
            msg="Insufficient balance"
            self.add_error('amount', msg)





