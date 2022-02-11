from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='salaries'),
    path('register/',views.register_salary,name='register_salary'),
    path('api/getusers',views.get_salary_for_items),
    path('api/checkselected',views.check_salary_user_already_exist)
]