from django.urls import path

from . import views

urlpatterns = [
    path('',views.login, name="login"),
    path('user/logout',views.logout,name="logout"),
    path('drivers/',views.drivers,name="drivers"),
    path('drivers/create/',views.create,name="create_driver"),
    path('drivers/<int:driver_id>/view',views.single_driver,name="single_driver"),
    path('drivers/<int:driver_id>/delete',views.delete_driver,name="delete_driver"),
    path('drivers/<int:driver_id>/edit',views.edit_driver,name="edit_driver"),
]