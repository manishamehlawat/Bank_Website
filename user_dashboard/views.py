from django.shortcuts import render
from bankuser.views import login
from .models import deposit
from .models import withdraw
from .models import total_money
from .models import account_details
from datetime import datetime








# Create your views here.
def deposite(request):
    if request.method=='POST':
         models_deposit=deposit()
         balance=request.POST.get('amount')
         account_no=request.session['account_number']
         models_deposit.Account_number=account_no
         models_deposit.Amount=balance
         models_deposit.Date=datetime.now()
         models_deposit.save()
         temp=total_money.objects.filter(Account_number=account_no).values_list('Balance',flat=True)
         bal=list(temp).pop(0)
         bal = bal+int(balance)
         total_money.objects.filter(Account_number=account_no).update(Balance=bal)
    return render(request,'dashboard.html')
def withdrawal(request):
    if request.method=='POST':
        models_withdraw=withdraw()
        balance=request.POST.get('amount')
        account_no=request.session['account_number']
        temp=total_money.objects.filter(Account_number=account_no).values_list('Balance',flat=True)
        bal=list(temp).pop(0)
        if bal> int(balance):
            models_withdraw.Account_number=account_no
            models_withdraw.Date=datetime.now()
            models_withdraw.Amount=balance
            models_withdraw.save()
            bal=bal-int(balance)
            total_money.objects.filter(Account_number=account_no).update(Balance=bal)
        else:
            return render(request,'dashboard.html', {'error':'not enough balance to withdraw'})
    return render(request,'dashboard.html')

def logout(request):
    del request.session['account_number']
    return render(request,'bank.html')

def dashboard(request):
    a = request.session['account_number']
    print(a)
    temp=total_money.objects.filter(Account_number=a).values_list('Balance',flat=True)
    bal=list(temp).pop(0)
    print(bal)
    return render(request,'dashboard.html', {'account_number': a, 'account_balance': bal})
