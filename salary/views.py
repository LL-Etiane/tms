from django.shortcuts import render
from .models import Salary
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib import messages
from django.shortcuts import redirect
import datetime
from django.contrib.auth.decorators import login_required

#serializers
from .serializers import DriverSerializer

#Models
from users.models import Driver
from .models import Salary

# Create your views here.

MONTHS_OF_THE_YEAR = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "Jully",
        "August",
        "September",
        "October",
        "November",
        "December",
      ]

@login_required
def index(request):
    if 'filter' in  request.GET:
        try:
            salaries = Salary.objects.filter(salary_for=request.GET['filter'])
        except Exception as e:
            print(e)
            salaries = []
    else:
        salaries = Salary.objects.all().order_by('-create_at')
    data = {'title':'Salries','salaries':salaries}
    
    return render(request,'salary/index.html',data)

@login_required
def register_salary(request):
    if request.method == 'POST':
        try:
            data = request.POST
            nsalary = Salary.objects.create(salary_for=data['salary_type'],description=data['description'],amount=data['amount'])
            if 'month' in data:
                if data['month'] in MONTHS_OF_THE_YEAR:
                    nsalary.month = data['month']
                else:
                    nsalary.month = datetime.date.today().strftime("%B")
            else:
                nsalary.month = datetime.date.today().strftime("%B")
            if 'salary_type_id' in data:
                nsalary.salary_for_id=data['salary_type_id']
            if 'isadvancement' in data:
                nsalary.advancement = True 
                
            nsalary.save()
            messages.info(request,"Salary successfully registered")
            return redirect('salaries') 
        except Exception as e:
            print(e)
            messages.error(request,"There was an error registering the salary. Please try again later")
            return redirect('register_salary')

    else:
        return render(request,'salary/create.html',{'title':'Register payment of new salary'})

@api_view()
def get_salary_for_items(request):
    salary_for = request.GET.get('salaryfor','')
    if str(salary_for).lower() == 'driver':
        data = Driver.objects.all().order_by('-date_created')
        ndata = DriverSerializer(data,many=True)
    else:
        return Response("Invalid supplied type",status=404)
    return Response(ndata.data)

@api_view()
def check_salary_user_already_exist(request):
    salary_type = request.GET.get('type','')
    salary_type_id = request.GET.get('type_id','')
    month = request.GET.get('month','')

    rdata = {'continue':False}
    
    if month is None:
        datetime.date.today().strftime("%B")
    try:
        test = Salary.objects.filter(salary_for=salary_type,salary_for_id=int(salary_type_id),month=month)
        
        if test and test.get().advancement == False:
            return Response(rdata)
        elif test and test.get().advancement:
            rdata['continue'] = True
            rdata['info'] = "This user has already recieve some advance salary of "+str(test.get().amount)+" Please go back to view on the driver to complete his payment from there"
            return Response(rdata)
        else:
            rdata['continue'] = True
            return Response(rdata)
    except Exception as e:
        print(e)
        rdata['continue'] = True
        return Response(rdata)

