from django.urls import path
from . import views

urlpatterns = [
    path('cars/',views.home, name="home"),
    path('cars/add',views.addCar,name="add_car"),
    path('cars/<int:car_id>/',views.singleCar,name='single_car'),
    path('cars/<int:car_id>/edit/',views.editCar,name='edit_car'),
    path('cars/<int:car_id>/delete',views.deleteCar,name='delete_car'),
    path('cars/<int:car_id>/documents',views.documents,name='car_documents'),
    path('cars/<int:car_id>/expense',views.car_expense,name='car_expense'),
    path('cars/<int:car_id>/revenue',views.car_revenue,name='car_revenue'),
    path('cars/<int:car_id>/alltransactions',views.all_transactions,name='car_transactions'),
    path('cars/expense/<int:expense_id>/view',views.single_expense_view,name='single_expense'),
    path('cars/revenue/<int:revenue_id>/view',views.single_reveue_view,name='single_revenue')
]