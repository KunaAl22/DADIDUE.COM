from django.http.response import HttpResponse
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import AbstractUser

from datetime import datetime
from home.models import Contact

from django.contrib import messages
from .models import *
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter


from django.contrib.auth import authenticate, login, logout
# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        description=request.POST.get('description')
        contact=Contact(name=name, email=email,number=number,description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'message has been send')
    return render(request,'contact.htm')     





def services(request):
    return render(request,'services.htm')
def index(request):
    return render(request,'index.htm')

def about(request):
    return render(request,'about.htm')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def audio(request):
    return render(request,'audio.html')	
def article(request):
    return render(request,'article.html')
def logo(request):
    return render(request,'logo.html')
def video(request):
    return render(request,'video.html')
def graphic(request):
    return render(request,'graphic.html')
def creative(request):
    return render(request,'creative.html')
def photo(request):
    return render(request,'photo.html')
def freelancer(request):
	return render(request,'freelancer.html')
def submitted(request):
	return render(request,'submitted.html')




def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	completed = orders.filter(status='Completed').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':completed,
	'pending':pending }

	return render(request, 'accounts/dashboard.htm', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.htm', {'products':products})


def registered(request):
	products = Product.objects.all()
	return render(request, 'accounts/registered.html')

def requested(request):
	products = Product.objects.all()
	return render(request, 'accounts/requested.html')


def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.htm',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/requested')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def createCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
	
			return redirect('/registered')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)

def handlelogin(request):
	if request.method=="POST":
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user=authenticate(username=loginusername,password=loginpassword)

		if user is not None:
			login(request, user)
			return redirect('home')

def login(request):
	return render(request,'login.html')

	

def logout(request):
	return HttpResponse('eafefea')

