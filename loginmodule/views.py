from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from test_app.models import Login,Bank_account,History,View,loan1,loan2,loan3
import time

#from django.core.exceptions import ObjectDoesNotException
def home(request):
	return render(request,'home.html')
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username,password=password)
	print('auth_view: ',user)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loginmodule/loggedin/')
	else:
		return HttpResponseRedirect('/loginmodule/invalidlogin/')


def loggedin(request):
	return render_to_response('loggedin.html', {"full_name":request.user.first_name})


def invalidlogin(request):
	return render_to_response('invalidlogin.html')

def logout(request):
	auth.logout(request) 
	return render_to_response('logout.html')

def transaction(request):
	return render(request, 'transaction.html')

def do_transaction(request):
	toAcc = request.POST.get('to')
	fromAcc = request.user.login.account_no
	amt = request.POST.get('amount')
	if((not toAcc.isdigit())):
		msg="Please Enter integer value in 'to' details...."
		return render(request,'transaction.html',{"msg":msg})
	if((not amt.isdigit())):
		msg="Please Enter integer value in 'amount' details...."
		return render(request,'transaction.html',{"msg":msg})
	amt=int(amt)
	try:
			msg=''
			toAcc = Login.objects.get(account_no=toAcc)
			f1=Bank_account.objects.get(account_no=request.user.login.account_no)
			t1=Bank_account.objects.get(account_no=toAcc.account_no)
			famt=Bank_account.objects.get(account_no=fromAcc).amount
			tamt=Bank_account.objects.get(account_no=toAcc.account_no).amount
			if(amt > famt):
				return render(request,'msg1.html',)
			else:
				tamt=tamt+amt
				famt=famt-amt
				f1.amount=famt
				t1.amount=tamt
				f1.save()	
				t1.save()
				now=time.strftime("%Y-%m-%d %H:%M")
				h=History(from_account_no=fromAcc,to_account_no=toAcc.account_no,amount_transfer=amt,time=now)
				h.save()
				return render(request,'msg.html',{"amounttt":f1.amount,"full_name":request.user.first_name,"msg":msg})
			
	except Login.DoesNotExist:
			msg="Please Enter valid 'to account' details...."
			return render(request,'transaction.html',{"msg":msg})

def display(request):
	fromAcc = request.user.login.account_no
	f1=Bank_account.objects.get(account_no=request.user.login.account_no)

	try:
		for acc in History.objects.filter(from_account_no=fromAcc):
			v=View(f_acc=acc.from_account_no,t_acc=acc.to_account_no,Debit=acc.amount_transfer,Credit=0,transaction_time=acc.time)
			v.save()
		for acc in History.objects.filter(to_account_no=fromAcc):
			v=View(f_acc=acc.from_account_no,t_acc=acc.to_account_no,Debit=0,Credit=acc.amount_transfer,transaction_time=acc.time)
			v.save()
		quary_result=View.objects.all().order_by('-transaction_time')
		return render(request,'display.html',{"quary_result":quary_result,"amount":f1.amount,"full_name":request.user.first_name})
	except History.DoesNotExist:
		return render(request,'transaction.html')
	finally:	
		View.objects.all().delete()

def profile(request):
	fromAcc = request.user.login.account_no
	one_row=Bank_account.objects.get(account_no=fromAcc)
	return render(request,'profile.html',{"one_row":one_row,"full_name":request.user.first_name})

def loan(request):
	uu1= loan1.objects.all()
	uu2= loan2.objects.all()
	uu3= loan3.objects.all()

	return render(request,'all.html',{"uu1":uu1,"uu2":uu2,"uu3":uu3})

def need_help(request):
	return render(request,'help.html')

def about_us(request):
	return render(request,'aboutus.html')

def changepw(request):
	return render(request,'changepw.html')

def changedb(request):
	password = request.POST.get('password')
	password2 = request.POST.get('password2')
	print(password)
	print(password2)
	if (password==password2):
		msg="successfully changed"
		c = request.user
		c.set_password(password)
		c.save()
		msg="successfully changed"
	else:
		msg="please put same password in both field"
	return render(request,'changed.html',{"msg":msg})