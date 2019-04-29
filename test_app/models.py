from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Login(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	account_no=models.IntegerField()


class Bank_account(models.Model):
	account_no=models.IntegerField()
	name=models.CharField(max_length=20)
	amount=models.IntegerField()
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	phone_no=models.IntegerField()
	email_id=models.EmailField(max_length=20)

class History(models.Model):
	from_account_no=models.IntegerField()
	to_account_no=models.IntegerField()
	amount_transfer=models.IntegerField()
	time= models.DateTimeField()

class View(models.Model):
	f_acc=models.IntegerField()
	t_acc=models.IntegerField()
	Debit=models.IntegerField()
	Credit=models.IntegerField()
	transaction_time = models.DateTimeField()


class loan1(models.Model):
	no=models.IntegerField()
	Time=models.IntegerField()
	interest_rate= models.IntegerField()

class loan2(models.Model):
	no=models.IntegerField()
	Time=models.IntegerField()
	interest_rate= models.IntegerField()

class loan3(models.Model):
	no=models.IntegerField()
	Time=models.IntegerField()
	interest_rate= models.IntegerField()