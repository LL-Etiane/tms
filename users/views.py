from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib import messages

#models
from .models import Driver

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/cars')
        return render(request,'users/login.html')
    if request.method == "POST":
        try:
            username = request.POST['name']
            password = request.POST['password']

            user = authenticate(username=username,password=password)

            if user is not None:
                user_login(request,user)
                return redirect("/cars")
            else:
                print(username,password)
                return render(request,'users/login.html',{"error":"Wrong username or password"})
        except Exception as e:
            print(e)
            return render(request,'users/login.html',{"error":"An error occured. Please try again"})

@login_required
def logout(request):
    user_logout(request)
    return redirect('/')

@login_required
def drivers(request):
    if request.method == 'GET':
        drivers  = Driver.objects.all().order_by('-date_created')
        data = {'title':'Drivers','drivers': drivers,'title':'Drivers'}
        return render(request,'users/drivers/drivers.html',data)

@login_required
def single_driver(request,driver_id):
    try: 
        driver = Driver.objects.get(id=driver_id);
        data = {'title':'View driver','driver':driver}
        return render(request,'users/drivers/single.html',data)
    except Exception as e:
        print(e)
        messages.error(request,'There was an error getting the requessted driver. Please try again later')
        return redirect('/drivers')

#delete driver view
@login_required
def delete_driver(request,driver_id):
    if request.method == 'POST':
        try: 
            driver = Driver.objects.get(id=driver_id);
            driver.delete()
            messages.success(request,'Driver successfully deleted')
            return redirect('/drivers')
        except Exception as e:
            print(e)
            messages.error(request,'There was an error deleting. Please try again later')
            return redirect('/drivers/'+str(driver_id)+'/view')
    else:
        return redirect('/drivers/'+str(driver_id)+'/view')

@login_required
def create(request):
    if request.method == 'POST':
        driverData = request.POST
        driverFiles = request.FILES
        try:
            driver_instance = Driver(name=driverData['name'],image=driverFiles['image'],driving_license=driverFiles['driving_license'],category=driverData['category'],nic=driverData['nic'])
            driver_instance.save()
            messages.success(request,'Driver successfully registered')
            return redirect('/drivers')
        except Exception as e:
            print(e)
            messages.error(request, 'There was an error registering. Make sure all the fields are filled')
            return redirect('create_driver')
    else:
        return render(request,'users/drivers/create.html',{'title':'Create driver'})


def edit_driver(request,driver_id):
    try:
        driver = Driver.objects.get(id=driver_id)
    except Exception as e:
        print (e)
        messages.error(request, 'An error occured while loading the requested driver. Plaese try again later')
        return redirect('drivers')
    if request.method == 'POST':
        pass 
    else:
        data = {'driver':driver,'title':'Edit driver details'} 
        return render(request,'users/drivers/edit.html',data)

        
