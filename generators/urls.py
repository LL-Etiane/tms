from django.urls import path

from . import views

urlpatterns = [
    path('',views.test, name="test"),
    path('revenue/<int:rev_id>',views.revenuePdf, name="generate_revenue_pdf"),
    path('expense/<int:exp_id>',views.expensePdf, name="generate_expense_pdf"),
]