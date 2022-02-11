from django.contrib.auth import login
from django.contrib.messages.api import success
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Car, CarDocument, Expense, Revenue
from users.models import Driver, Shift
from .forms import CarForm
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

@login_required
def home(request):
    cars = Car.objects.all().order_by('-date_created')
    data = {"cars":cars,'title':'Cars'}
    return render(request,'cars/index.html',data)

@login_required
def addCar(request):
    drivers = Driver.objects.filter(car=None)
    shifts = Shift.objects.all()
    form = CarForm()
    data = {'form':form,'drivers':drivers,'shifts':shifts,'title':"Add new car"}
    if request.method == 'GET': 
        return render(request,'cars/add.html',data)
    if request.method == 'POST':
        form = CarForm(request.POST)
        data['old'] = request.POST
        try:
            car = Car.objects.create(matricule=request.POST['matricule'],car_type=request.POST['car_type'],date_bought=request.POST['date_bought'],date_put_to_use=request.POST['date_put_to_use'],price=request.POST['price'],kilometres_bought_with=request.POST['kilometres_bought_with'])
        except Exception as e:
            print(e)
            messages.error(request,"An error occured while creating. Make sure you are not creating something which alreading exist. If the error persist, contact Admin")
            return render(request,'cars/add.html',data)
        for shift in shifts:
            if request.POST['driver_'+str(shift.type)] != '':
                id = int(request.POST['driver_'+str(shift.type)])
                driver = Driver.objects.get(id=id)
                driver.car.add(car) 
                shift.driver_set.add(driver)
        messages.success(request,"Car successfully added")
        return redirect('/cars')

@login_required 
def singleCar(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        revenues = car.revenue_set.all().order_by('-date')[:5]
        expenses = car.expense_set.all().order_by('-date')[:5]
        data = {'car':car,'title':'Car details','revenues':revenues,'expenses':expenses}
        return render(request, 'cars/single.html',data)
    except Exception as e:
        print(e)
        return redirect('/cars')

@login_required
def editCar(request, car_id):
    drivers = Driver.objects.filter(car=None)
    shifts = Shift.objects.all()
    if request.method == 'GET':
        try:
            car = Car.objects.get(id=car_id)
            driver_set = car.driver_set.all()
            data = {'car':car,'drivers':drivers,'shifts':shifts,'driver_set':driver_set,'title': 'Edit car'}
            return render(request, 'cars/edit.html',data)
        except Exception as e:
            print(e)
            return redirect('/cars')
    if request.method == 'POST':
        try:
            car = Car.objects.get(id=car_id)
            car.matricule = request.POST['matricule']
            car.car_type = request.POST['car_type']
            car.date_bought = request.POST['date_bought']
            car.date_put_to_use = request.POST['date_put_to_use']
            car.price = request.POST['price']
            car.kilometres_bought_with = request.POST['kilometres_bought_with']
            car.save()
            for shift in shifts:
                if request.POST['driver_'+str(shift.type)] != '':
                    if len(car.driver_set.filter(shift=shift)):
                        car.driver_set.filter(shift=shift)[0].car.remove(car)
                    id = int(request.POST['driver_'+str(shift.type)])
                    driver = Driver.objects.get(id=id)
                    driver.car.add(car) 
                    shift.driver_set.add(driver)
            messages.success(request,"Car successfully edited")
            return redirect('/cars')
        except Exception as e:
            print(e)
            messages.error(request,"An error occured while trying to edit. If the error persist, contact Admin")
            return redirect('/cars')

@login_required
@permission_required
def deleteCar(request,car_id):
    if request.method == 'POST':
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            messages.success(request, "Car successfully deleted")
            return redirect('/cars')
        except Exception as e:
            print(e)
            return redirect('/cars')

@login_required
def documents(request, car_id):
    if request.method == 'POST':
        try: 
            car = Car.objects.get(id=car_id)
            doc = CarDocument.objects.create(type=request.POST['doc'],amount=request.POST['amount'],description=request.POST['description'],date_paid=request.POST['date_paid'],expiry_date=request.POST['expiry_date'],car=car,image=request.FILES['document_image'])
            messages.success(request,"Document successully added")
            return redirect('/cars/'+str(car_id)+'documents')
        except Exception as e: 
            print(e)
            messages.error(request, "An error occured while saving document. Please try again. if this persit, contact admin")
            return redirect('/cars/'+str(car_id)) 
    else: 
        try:
            car = Car.objects.get(id=car_id)
            documents = car.cardocument_set.all().order_by('-date_paid')
            data = {'car':car,'title':'Car details','documents':documents,'title':'Car documents'}
            return render(request, 'cars/documents/index.html',data)
        except Exception as e:
            messages.error(request, "There was an error. Make sure car id is provided and is valid")
            return redirect('/cars/')
@login_required
def car_expense(request, car_id):
    try: 
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        messages.error(request, "There was an error. Make sure car id is provided and is valid")
        return redirect('/cars/')
    if request.method == 'POST':
        try:
            Expense.objects.create(car=car,name=request.POST['name'],amount=request.POST['amount'],description=request.POST['description'])
            messages.success(request,"Expense successfully added")
            return redirect('/cars/'+str(car_id))
        except Exception as e:
            print(e)
            messages.error(request,'There was an error while saving. Please make sure all fields are filled and try again')
            return redirect(request.META['HTTP_REFERER'])
    else:
        data = {'car':car, 'title':'Add car expense'}
        return render(request,'cars/transactions/expense.html',data)

@login_required
def car_revenue(request, car_id):
    try: 
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        messages.error(request, "There was an error. Make sure car id is provided and is valid")
        return redirect('/cars/')
    if request.method == 'POST':
        try:
            Revenue.objects.create(car=car,name=request.POST['name'],amount=request.POST['amount'],description=request.POST['description'])
            messages.success(request,"Revenue successfully added")
            return redirect('/cars/'+str(car_id))
        except Exception as e:
            print(e)
            messages.error(request,'There was an error while saving. Please make sure all fields are filled and try again')
            return redirect(request.META['HTTP_REFERER'])
    else:
        data = {'car':car, 'title':'Add car revenue'}
        return render(request,'cars/transactions/revenue.html',data)


@login_required
def all_transactions(request, car_id):
    try: 
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        messages.error(request, "There was an error. Make sure car id is provided and is valid")
        return redirect('/cars/')

    if request.method == 'POST':
        pass
    else:
        expenses = car.expense_set.all().order_by('-date')
        total_exp = car.expense_set.aggregate(Sum('amount'))['amount__sum']
        revenues = car.revenue_set.all().order_by('-date')
        total_rev = car.revenue_set.aggregate(Sum('amount'))['amount__sum']
        result  = total_rev - total_exp
        data = {'title':'Transactions detials','car':car,'revenues':revenues,'expenses':expenses,'total_exp':total_exp,'total_rev':total_rev,'result':result}
        return render(request,'cars/transactions/all_records.html',data)

def single_expense_view(request, expense_id):
    try:
        exp = Expense.objects.get(id=expense_id)
        data = {'title':'Expense details','exp':exp}
        return render(request, 'cars/transactions/single_expense.html',data)
    except Exception as e:
        print(e)
        messages.error(request, "There was an error getting the requested data. Plese try again later")
        return redirect('/cars/')

def single_reveue_view(request, revenue_id):
    try:
        rev = Revenue.objects.get(id=revenue_id)
        data = {'title':'Revenue details','rev':rev}
        return render(request, 'cars/transactions/single_revenue.html',data)
    except Exception as e:
        print(e)
        messages.error(request, "There was an error getting the requested data. Plese try again later")
        return redirect('/cars/')