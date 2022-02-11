from django.http import HttpResponse
from django.forms.models import model_to_dict
from cars.models import Revenue, Expense
from django.contrib.auth.decorators import login_required

import datetime

from .utils import generatePDF

# Create your views here.
def test(request):
    rev = Revenue.objects.get(id=1)
    test = model_to_dict(rev)
    test['date'] = rev.date
    test['generated_date'] = datetime.date.today()
    test['generated_time'] = datetime.datetime.now().time()
    test['by'] = 'etiane'
    print(test)
    pdf = generatePDF('generators/pdf.html',test)
    if pdf:
        response = HttpResponse(pdf.getvalue(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="sample.pdf"'
        return response
    else: 
        print(pdf.err)
        return HttpResponse("errror")


@login_required
def revenuePdf(request,rev_id):
    try:
        rev_data = Revenue.objects.get(id=rev_id)
        data = model_to_dict(rev_data)
        data['date'] =rev_data.date
        data['generated_date'] = datetime.date.today()
        data['generated_time'] = datetime.datetime.now().time()
        data['by'] = request.user
        rev_pdf = generatePDF('generators/revenue.html',data)
        if rev_pdf:
            response = HttpResponse(rev_pdf.getvalue(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="revenue_reciept.pdf"'
            return response
        else: 
            print(rev_pdf.err)
            return HttpResponse("errror")
    except Exception as e:
        print(e)
        return HttpResponse("There was an error please try again later")

@login_required
def expensePdf(request,exp_id):
    try:
        exp_data = Expense.objects.get(id=exp_id)
        data = model_to_dict(exp_data)
        data['date'] =exp_data.date
        data['generated_date'] = datetime.date.today()
        data['generated_time'] = datetime.datetime.now().time()
        data['by'] = request.user
        exp_pdf = generatePDF('generators/expense.html',data)
        if exp_pdf:
            response = HttpResponse(exp_pdf.getvalue(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="expense_reciept.pdf"'
            return response
        else: 
            print(exp_pdf.err)
            return HttpResponse("errror")
    except Exception as e:
        print(e)
        return HttpResponse("There was an error please try again later")