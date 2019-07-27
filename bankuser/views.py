from django.shortcuts import render,redirect
from .models import banking
from user_dashboard.models import deposit,withdraw,total_money,account_details
from datetime import datetime
import random
import string
from pip._vendor.requests.api import delete

# Create your views here.
def homepage(request):
    
    return render(request,'bank.html')
def signup(request):
    if request.method=='POST':
        
        models_bank=banking()
        models_deposit=deposit()
        models_total_money=total_money()
        models_account_details=account_details()
        models_withdraw=withdraw()
        
        temp=request.POST.get('email')
        a=banking.objects.filter(Email=temp)
        
        if a.exists():
            print('user already present')
        else:
            models_bank.Name=request.POST.get('username')
            models_bank.Email=request.POST.get('email')
            models_bank.Password=request.POST.get('password')
            models_bank.Phone_no=request.POST.get('phone_number')
            models_bank.Date=datetime.now()
            models_bank.Count=0
            models_account=''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(14))
            account_number=models_account
            print(account_number)
            models_bank.save()
            models_account_details.Account_number=models_account
            models_account_details.Email=request.POST.get('email')
            models_account_details.Phone_no=request.POST.get('phone_number')
            models_account_details.save()
            models_deposit.Account_number=models_account
            models_deposit.Amount=0
            models_deposit.Date=datetime.now()
            models_deposit.save()
            models_total_money.Account_number=models_account
            models_total_money.Balance=0
            models_total_money.save()
            models_withdraw.Account_number=models_account
            models_withdraw.Amount=0
            models_withdraw.Date=datetime.now()
            models_withdraw.save()
            
    return render(request,'bank.html')




def login(request):
    
    if request.method=='POST':
        username=request.POST.get('email')
        pwd=request.POST.get('password')
        username_exist=banking.objects.filter(Email=username)
        
        
        if not username_exist.exists():
            print('enter valid email_id')
            return render(request,'bank.html',{'var1':'email doesnot exists'})
        
        
        if username_exist.exists():
            pwd_exist=banking.objects.filter(Email=username).filter(Password=pwd)
            ac=account_details.objects.filter(Email=username).values_list('Account_number',flat=True)
            account_no=list(ac).pop(0)
            print(account_no)
            request.session['account_number'] = account_no
            count=banking.objects.filter(Email=username).values_list('Count',flat=True)
            
            inc = list(count).pop(0)
            print(inc)
            
            
            if pwd_exist.exists() and inc<3:
                print('login successful')
                return redirect('/dashboard')
            
            
            if inc>=3:
                print('count exceeds')
                return render (request,'bank.html', {'error': 'Account Locked'})
            
            
            if not pwd_exist.exists():
                inc=inc+1
                banking.objects.filter(Email=username).update(Count=inc)
                return render(request,'bank.html',{'var2':'you have ', 'var3': (3-inc), 'var4': ' attempts left'})
            
    return render (request,'bank.html')

